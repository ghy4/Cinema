import sys
from os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
from flask import Flask, render_template
from flask_mail import Mail
from config import Config
from src.extensions import db
from sqlalchemy import text
from .routes.auth import auth_bp
from .routes.movies import movies_bp
from .routes.bookings import bookings_bp
from .routes.client import client_bp
from .routes.operator import operator_bp
from .routes.admin import admin_bp
from flask_login import LoginManager
import logging
from datetime import datetime, timedelta
from src.models.movie import Movie
from src.models.user import User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
handler.setFormatter(formatter)
if not app.logger.hasHandlers():
    app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

mail = Mail(app)

app.register_blueprint(auth_bp)
app.register_blueprint(movies_bp)
app.register_blueprint(bookings_bp)
app.register_blueprint(client_bp)
app.register_blueprint(operator_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    today = datetime.utcnow().date()
    thirty_days_ago = today - timedelta(days=30)
    movies = Movie.query.filter(Movie.release_date != None, Movie.release_date >= thirty_days_ago).all()
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)