from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()

Base = db.Model
mail = Mail()