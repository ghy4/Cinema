from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models.booking import Booking
from src.models.cinema import Cinema
from src.models.movie import Movie
from src.extensions import db

operator_bp = Blueprint('operator', __name__)

@operator_bp.route('/operator/dashboard')
def dashboard():
    bookings = Booking.get_all_bookings()
    return render_template('operator_dashboard.html', bookings=bookings)

@operator_bp.route('/operator/bookings/<int:booking_id>/modify', methods=['GET', 'POST'])
def modify_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    if request.method == 'POST':
        new_date = request.form.get('date')
        new_time = request.form.get('time')
        new_seats = request.form.get('seats')
        if new_date:
            booking.date = new_date
        if new_time:
            booking.time = new_time
        if new_seats:
            booking.seats = new_seats
        db.session.commit()
        flash('Booking modified successfully!', 'success')
        return redirect(url_for('operator.dashboard'))
    return render_template('modify_booking.html', booking=booking)

@operator_bp.route('/operator/bookings/<int:booking_id>/cancel', methods=['POST'])
def cancel_booking(booking_id):
    Booking.cancel_booking(booking_id)
    flash('Booking canceled successfully!', 'success')
    return redirect(url_for('operator.dashboard'))