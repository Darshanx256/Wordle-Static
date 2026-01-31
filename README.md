# Wordle Static Website

This is the standalone web version of the Wordle Game Bot landing page. It is designed to be hosted independently of the Discord bot.

## Features
-   **Live Server Count**: Automatically fetches the live server count from the main bot via an API hook.
-   **Responsive Design**: Optimized for both mobile and desktop.
-   **Terms & Privacy**: Includes standard legal templates for Discord bot websites.

## Deployment

### 🐳 Docker
Build and run locally:
```bash
docker build -t wordle-web .
docker run -p 8080:8080 wordle-web
```

### ☁️ Google App Engine
Deploy with one command:
```bash
gcloud app deploy
```

### 🚀 Other Platforms
The repository includes a `Procfile` for Heroku/Render and can be hosted on any platform that supports Python/Flask.

## Configuration
The site fetches live stats from: `https://discord-wordle-bot-0wll.onrender.com/api/stats`. 
If you host your own version of the main bot, update the fetch URL in `static/index.html`.
