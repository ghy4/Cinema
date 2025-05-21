from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
import re

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def validate_booking_data(data):
    required_fields = ['cinema', 'date', 'time', 'seats']
    return all(field in data for field in required_fields)

def hash_password(password):
    return generate_password_hash(password)

def check_hashed_password(password, hashed_password):
    return check_password_hash(hashed_password, password)