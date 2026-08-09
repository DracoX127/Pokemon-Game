from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
import sqlite3
import datetime
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'pokemon-game-secret-key-12345')
CORS(app)
bcrypt = Bcrypt(app)

# Use env var for DB path, default to local
DB_FILE = os.environ.get('DB_FILE', 'accounts.db')

def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
    db.execute('CREATE TABLE IF NOT EXISTS saves (user_id INTEGER PRIMARY KEY, save_data TEXT, updated_at DATETIME DEFAULT CURRENT_TIMESTAMP)')
    db.commit()
    db.close()

def utc_now_text():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

def decode_auth_payload():
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return None, ({'message': 'No token provided'}, 401)
    token = auth.split(' ', 1)[1]
    try:
        return jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256']), None
    except jwt.ExpiredSignatureError:
        return None, ({'message': 'Token expired. Please login again.'}, 401)

def summarize_save(save_data):
    try:
        data = json.loads(save_data or '{}')
    except json.JSONDecodeError:
        return {
            'valid': False,
            'trainer': 'Unknown',
            'message': 'Save data is not valid JSON'
        }

    pokemon = data.get('pokemon') or {}
    inventory = data.get('inventory') or {}
    badges = data.get('badges') or []
    pokedex_caught = data.get('pokedex_caught') or []
    fainted = sum(1 for stats in pokemon.values() if isinstance(stats, dict) and stats.get('hp', 0) <= 0)
    strongest = None
    if isinstance(pokemon, dict) and pokemon:
        strongest = max(
            pokemon.items(),
            key=lambda item: item[1].get('dm', 0) if isinstance(item[1], dict) else 0
        )[0]

    return {
        'valid': True,
        'save_version': data.get('save_version', 1),
        'saved_at': data.get('saved_at'),
        'trainer': data.get('name', 'Trainer'),
        'location': data.get('location', 'Unknown'),
        'team_count': len(pokemon) if isinstance(pokemon, dict) else 0,
        'fainted_count': fainted,
        'strongest': strongest,
        'money': data.get('money', 0),
        'trophies': data.get('trophies', 0),
        'badges_count': len(badges) if isinstance(badges, list) else 0,
        'pokedex_caught': len(pokedex_caught) if isinstance(pokedex_caught, list) else 0,
        'inventory_types': len(inventory) if isinstance(inventory, dict) else 0,
    }

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'version': '2.0'})

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username', '').strip()
        password = data.get('password', '')
        if not username or not password:
            return jsonify({'message': 'Username and password required'}), 400
        if len(username) < 3 or len(username) > 20:
            return jsonify({'message': 'Username must be 3-20 characters'}), 400
        if len(password) < 4:
            return jsonify({'message': 'Password must be at least 4 characters'}), 400
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        db = get_db()
        try:
            db.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, pw_hash))
            db.commit()
            return jsonify({'message': 'User registered successfully'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'message': 'Username already taken'}), 400
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username', '').strip()
        password = data.get('password', '')
        if not username or not password:
            return jsonify({'message': 'Username and password required'}), 400
        db = get_db()
        try:
            user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            if user and bcrypt.check_password_hash(user['password_hash'], password):
                token = jwt.encode({
                    'user_id': user['id'],
                    'username': user['username'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=72)
                }, app.config['SECRET_KEY'], algorithm='HS256')
                return jsonify({'token': token, 'username': user['username']})
            return jsonify({'message': 'Invalid username or password'}), 401
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/save', methods=['POST'])
def save():
    try:
        payload, auth_error = decode_auth_payload()
        if auth_error:
            return jsonify(auth_error[0]), auth_error[1]
        incoming = request.json or {}
        save_data = incoming.get('save_data', '')
        summary = summarize_save(save_data)
        if not summary.get('valid'):
            return jsonify({'message': summary['message']}), 400
        updated_at = utc_now_text()
        db = get_db()
        try:
            db.execute('INSERT OR REPLACE INTO saves (user_id, save_data, updated_at) VALUES (?, ?, ?)',
                       (payload['user_id'], save_data, updated_at))
            db.commit()
            return jsonify({
                'message': 'Save successful',
                'updated_at': updated_at,
                'byte_count': len(save_data.encode('utf-8')),
                'summary': summary
            })
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/load', methods=['GET'])
def load():
    try:
        payload, auth_error = decode_auth_payload()
        if auth_error:
            return jsonify(auth_error[0]), auth_error[1]
        db = get_db()
        try:
            save = db.execute('SELECT save_data, updated_at FROM saves WHERE user_id = ?', (payload['user_id'],)).fetchone()
            if save:
                save_data = save['save_data']
                return jsonify({
                    'save_data': save_data,
                    'updated_at': save['updated_at'],
                    'byte_count': len(save_data.encode('utf-8')),
                    'summary': summarize_save(save_data)
                })
            return jsonify({'message': 'No save found'}), 404
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/save-info', methods=['GET'])
def save_info():
    try:
        payload, auth_error = decode_auth_payload()
        if auth_error:
            return jsonify(auth_error[0]), auth_error[1]
        db = get_db()
        try:
            save = db.execute('SELECT save_data, updated_at FROM saves WHERE user_id = ?', (payload['user_id'],)).fetchone()
            if not save:
                return jsonify({'message': 'No save found'}), 404
            save_data = save['save_data']
            return jsonify({
                'updated_at': save['updated_at'],
                'byte_count': len(save_data.encode('utf-8')),
                'summary': summarize_save(save_data)
            })
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/accounts', methods=['GET'])
def list_accounts():
    """Public endpoint to view registered account usernames (no passwords)."""
    try:
        db = get_db()
        try:
            users = db.execute('''
                SELECT users.username, users.created_at, saves.updated_at
                FROM users
                LEFT JOIN saves ON saves.user_id = users.id
                ORDER BY users.created_at DESC
            ''').fetchall()
            accounts = [
                {'username': u['username'], 'created': u['created_at'], 'save_updated_at': u['updated_at']}
                for u in users
            ]
            return jsonify({'accounts': accounts, 'total': len(accounts)})
        finally:
            db.close()
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/me', methods=['GET'])
def me():
    """Get current user info."""
    try:
        auth = request.headers.get('Authorization', '')
        if not auth.startswith('Bearer '):
            return jsonify({'message': 'No token'}), 401
        token = auth.split(' ')[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'user_id': payload['user_id'], 'username': payload.get('username', 'unknown')})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired'}), 401
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
