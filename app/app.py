from flask import Flask
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "super_secret_key_123"  # Required for sessions
    register_routes(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
