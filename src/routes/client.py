from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models.booking import Booking
from flask_login import current_user
from src.models.user import User
from src.models.movie import Movie

client_bp = Blueprint('client', __name__)

@client_bp.route('/dashboard')
def dashboard():
    user_id = current_user.id
    bookings = Booking.get_user_bookings(user_id)
    return render_template('client_dashboard.html', bookings=bookings)

@client_bp.route('/view_booking/<int:booking_id>')
def view_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    if booking:
        return render_template('view_booking.html', booking=booking)
    else:
        flash('Booking not found.', 'error')
        return redirect(url_for('client.dashboard'))

@client_bp.route('/edit_booking/<int:booking_id>', methods=['GET', 'POST'])
def edit_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    if request.method == 'POST':
        new_movie_id = request.form.get('movie_id')
        new_showtime = request.form.get('showtime')
        success = Booking.update_booking(booking_id, new_movie_id, new_showtime)
        if success:
            flash('Booking updated successfully.', 'success')
            return redirect(url_for('client.dashboard'))
        else:
            flash('Failed to update booking. Please try again.', 'error')
    movies = Movie.get_all_movies()
    return render_template('edit_booking.html', booking=booking, movies=movies)

@client_bp.route('/cancel_booking/<int:booking_id>', methods=['POST'])
def cancel_booking(booking_id):
    success = Booking.cancel_booking(booking_id)
    if success:
        flash('Booking cancelled successfully.', 'success')
    else:
        flash('Failed to cancel booking. Please try again.', 'error')
    return redirect(url_for('client.dashboard'))
