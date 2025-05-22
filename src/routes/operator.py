from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models.booking import Booking
from src.models.movie import Movie
from src.extensions import db
from src.utils.decorators import roles_required

operator_bp = Blueprint('operator', __name__)

@operator_bp.route('/operator/dashboard')
@roles_required('Manager', 'Employee')
def dashboard():
    bookings = Booking.get_all_bookings()
    return render_template('operator_dashboard.html', bookings=bookings)

@operator_bp.route('/operator/bookings/<int:booking_id>/view')
@roles_required('Manager', 'Employee')
def view_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    return render_template('view_booking.html', booking=booking)

@operator_bp.route('/operator/bookings/<int:booking_id>/edit', methods=['GET', 'POST'])
@roles_required('Manager', 'Employee')
def edit_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    if request.method == 'POST':
        new_seats = request.form.get('seats')
        new_email = request.form.get('email')
        if new_seats:
            booking.seats = int(new_seats)
        if new_email:
            booking.email = new_email
        db.session.commit()
        flash('Booking updated successfully!', 'success')
        return redirect(url_for('operator.dashboard'))
    return render_template('edit_booking.html', booking=booking)

@operator_bp.route('/operator/bookings/<int:booking_id>/cancel', methods=['POST'])
@roles_required('Manager', 'Employee')
def cancel_booking(booking_id):
    Booking.cancel_booking(booking_id)
    flash('Booking canceled successfully!', 'success')
    return redirect(url_for('operator.dashboard'))