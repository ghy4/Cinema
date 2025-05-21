import json

def format_currency(amount):
    return f"${amount:.2f}"

def calculate_discounted_price(original_price, discount_percentage):
    return original_price - (original_price * (discount_percentage / 100))

def generate_ticket_id(user_id, booking_id):
    return f"TICKET-{user_id}-{booking_id}"

def is_valid_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def sanitize_input(user_input):
    import html
    return html.escape(user_input)