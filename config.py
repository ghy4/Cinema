from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = int(587)
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'poo.proiect@gmail.com'
    MAIL_PASSWORD = 'egfyndgvjihozhtv'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Qwerty12345@localhost:5432/flask_db'