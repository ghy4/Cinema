from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from flask_login import login_required
from src.models.booking import Booking
from src.models.movie import Movie
from services.payment_service import create_payment_intent
from services.email_service import send_confirmation_email
from flask_login import current_user
from src.extensions import db

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/book_tickets/<int:movie_id>', methods=['GET', 'POST'])
def book_tickets(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        seats = request.form.get('seats')
        email = request.form.get('email')
        payment_success = True
        if payment_success:
            flash('Payment successful! Your tickets are booked.', 'success')
            booking = Booking(
            user_id=current_user.id,
            movie_id=movie.id,
            seats=seats,
            email=email
            )
            db.session.add(booking)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash('Payment failed. Please try again.', 'danger')
    return render_template('booking.html', movie=movie)

@bookings_bp.route('/book', methods=['POST'])
def book_ticket():
    data = request.json
    booking = Booking(
        user_id=data['user_id'],
        movie_id=data['movie_id'],
        cinema_id=data['cinema_id'],
        showtime=data['showtime'],
        seats=data['seats'],
        total_price=data['total_price']
    )
    
    if booking.save():
        payment_success = create_payment_intent(data['payment_info'])
        if payment_success:
            send_confirmation_email(booking.user_id, booking.id)
            return jsonify({'message': 'Booking successful!', 'booking_id': booking.id}), 201
        else:
            return jsonify({'message': 'Payment failed. Please try again.'}), 400
    return jsonify({'message': 'Booking failed. Please check your details.'}), 400

@bookings_bp.route('/history/<user_id>', methods=['GET'])
def booking_history(user_id):
    bookings = Booking.get_user_bookings(user_id)
    return jsonify(bookings), 200

@bookings_bp.route('/cancel/<booking_id>', methods=['DELETE'])
def cancel_booking(booking_id):
    booking = Booking.get_by_id(booking_id)
    if booking and booking.cancel():
        return jsonify({'message': 'Booking cancelled successfully.'}), 200
    return jsonify({'message': 'Cancellation failed. Booking not found or already cancelled.'}), 404