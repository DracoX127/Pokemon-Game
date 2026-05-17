from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
import sqlite3
import datetime
import os

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
        auth = request.headers.get('Authorization', '')
        if not auth.startswith('Bearer '):
            return jsonify({'message': 'No token provided'}), 401
        token = auth.split(' ')[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        db = get_db()
        try:
            db.execute('INSERT OR REPLACE INTO saves (user_id, save_data, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP)',
                       (payload['user_id'], request.json.get('save_data', '')))
            db.commit()
            return jsonify({'message': 'Save successful'})
        finally:
            db.close()
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired. Please login again.'}), 401
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/load', methods=['GET'])
def load():
    try:
        auth = request.headers.get('Authorization', '')
        if not auth.startswith('Bearer '):
            return jsonify({'message': 'No token provided'}), 401
        token = auth.split(' ')[1]
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        db = get_db()
        try:
            save = db.execute('SELECT save_data FROM saves WHERE user_id = ?', (payload['user_id'],)).fetchone()
            if save:
                return jsonify({'save_data': save['save_data']})
            return jsonify({'message': 'No save found'}), 404
        finally:
            db.close()
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token expired. Please login again.'}), 401
    except Exception as e:
        return jsonify({'message': f'Server error: {str(e)}'}), 500

@app.route('/api/accounts', methods=['GET'])
def list_accounts():
    """Public endpoint to view registered account usernames (no passwords)."""
    try:
        db = get_db()
        try:
            users = db.execute('SELECT username, created_at FROM users ORDER BY created_at DESC').fetchall()
            accounts = [{'username': u['username'], 'created': u['created_at']} for u in users]
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
