import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/terms')
@app.route('/tos')
def terms():
    return send_from_directory(app.static_folder, 'tos.html')

@app.route('/privacy')
def privacy():
    return send_from_directory(app.static_folder, 'privacy.html')

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    from waitress import serve
    print(f"🌍 Starting Web Server on port {port}...")
    serve(app, host='0.0.0.0', port=port)
