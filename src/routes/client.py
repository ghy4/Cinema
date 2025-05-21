from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models.booking import Booking
from src.models.user import User
from src.models.movie import Movie

client_bp = Blueprint('client', __name__)

@client_bp.route('/dashboard')
def dashboard():
    user_id = request.args.get('user_id')
    bookings = Booking.get_user_bookings(user_id)
    return render_template('client_dashboard.html', bookings=bookings)

@client_bp.route('/bookings')
def bookings():
    user_id = request.args.get('user_id')
    bookings = Booking.get_user_bookings(user_id)
    return render_template('client_dashboard.html', bookings=bookings)

@client_bp.route('/cancel_booking/<int:booking_id>', methods=['POST'])
def cancel_booking(booking_id):
    success = Booking.cancel_booking(booking_id)
    if success:
        flash('Booking cancelled successfully.', 'success')
    else:
        flash('Failed to cancel booking. Please try again.', 'error')
    return redirect(url_for('client.dashboard'))
