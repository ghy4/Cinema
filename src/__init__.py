from flask import Flask
from config import Config
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Import blueprints inside the function to avoid circular imports
    from .routes.movies import movies_bp
    app.register_blueprint(movies_bp)

    return app