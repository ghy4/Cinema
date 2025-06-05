from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user
from utils.convertors import user_to_person
from src.models.user import Employee, Manager, Customer

def roles_required_oop(*classes):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('You must be logged in.', 'danger')
                return redirect(url_for('index'))
            person = user_to_person(current_user)
            if not isinstance(person, classes):
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator