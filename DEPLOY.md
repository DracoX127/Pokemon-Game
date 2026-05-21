# Pokémon Game - Cloud Deployment Guide

## Quick Deploy to Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Render will auto-detect `render.yaml` and configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT utils.server:app`
6. Click "Create Web Service"
7. Copy the deployed URL (e.g., `https://pokemon-game-server.onrender.com`)

## Update Game Client

After deployment, update `core/main.py` line 92:
```python
SERVER_URL = "https://your-render-url.onrender.com/api"
```

## Deploy to Railway

1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Railway will auto-detect `requirements.txt` and `Procfile`
4. Add environment variables:
   - `SECRET_KEY`: (generate a random string)
   - `DB_FILE`: `/data/accounts.db`
5. Deploy
6. Copy the deployed URL

## Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Start server
python utils/server.py

# Start game (in another terminal)
python main.py
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | JWT signing key | `pokemon-game-secret-key-12345` |
| `DB_FILE` | SQLite database path | `accounts.db` |
| `PORT` | Server port | `5001` |
