from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import sqlite3
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pokemon-game-secret-key-12345'
bcrypt = Bcrypt(app)
DB_FILE = 'accounts.db'

def get_db():
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS saves (user_id INTEGER PRIMARY KEY, save_data TEXT, updated_at DATETIME)')
    db.commit()
    db.close()

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    pw_hash = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    db = get_db()
    try:
        cursor = db.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (data['username'], pw_hash))
        db.commit()
        return jsonify({'message': 'User registered'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'Username taken'}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (data['username'],)).fetchone()
    if user and bcrypt.check_password_hash(user['password_hash'], data['password']):
        token = jwt.encode({'user_id': user['id'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/save', methods=['POST'])
def save():
    token = request.headers.get('Authorization').split(" ")[1]
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    db = get_db()
    db.execute('INSERT OR REPLACE INTO saves (user_id, save_data, updated_at) VALUES (?, ?, ?)', 
               (payload['user_id'], request.json['save_data'], datetime.datetime.utcnow()))
    db.commit()
    return jsonify({'message': 'Saved'})

@app.route('/api/load', methods=['GET'])
def load():
    token = request.headers.get('Authorization').split(" ")[1]
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    db = get_db()
    save = db.execute('SELECT save_data FROM saves WHERE user_id = ?', (payload['user_id'],)).fetchone()
    return jsonify({'save_data': save['save_data']}) if save else jsonify({'message': 'No save'}), 404

if __name__ == '__main__':
    init_db()
    app.run(port=5001)
