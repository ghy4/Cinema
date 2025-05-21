from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@example.com'

mail = Mail(app)

def send_ticket_confirmation(email, ticket_details):
    subject = "Your Ticket Confirmation"
    body = f"Thank you for your purchase! Here are your ticket details:\n{ticket_details}"
    msg = Message(subject, recipients=[email])
    msg.body = body
    mail.send(msg)


def send_confirmation_email(email, booking_id):
    subject = "Booking Confirmation"
    body = f"Your booking (ID: {booking_id}) was successful!"
    msg = Message(subject, recipients=[email])
    msg.body = body
    mail.send(msg)