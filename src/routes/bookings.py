from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from flask_login import login_required
from flask_mail import Mail, Message
from src.models.booking import Booking
from src.models.movie import Movie
from flask_login import current_user
from src.extensions import db, mail
from services.qr_code_service import generate_qr_code_bytes
from datetime import datetime

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/book_tickets/<int:movie_id>', methods=['GET', 'POST'])
@login_required
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
            booking_time=datetime.utcnow(),
            seats=seats,
            email=email
            )
            db.session.add(booking)
            db.session.commit()
            qr_data = f"Booking ID: {booking.id}, Movie: {movie.title}, Seats: {seats}"
            qr_bytes = generate_qr_code_bytes(qr_data)

            msg = Message(
                subject='Your Cinema Booking Confirmation',
                sender='poo.proiect@gmail.com',
                recipients=[email]
            )
            msg.body = f"Thank you for your booking!\n\nMovie: {movie.title}\nSeats: {seats}\nBooking ID: {booking.id}\n\nPlease find your QR code attached."
            msg.attach('ticket_qr.png', 'image/png', qr_bytes)
            mail.send(msg)
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
        total_price=data['total_price'],
        email=data['email']
    )

    db.session.add(booking)
    db.session.commit()

    payment_success = True
    if payment_success:
        movie = Movie.query.get(booking.movie_id)
        qr_data = f"Booking ID: {booking.id}, Movie: {movie.title}, Seats: {booking.seats}"
        qr_bytes = generate_qr_code_bytes(qr_data)
        msg = Message(
            subject='Your Cinema Booking Confirmation',
            sender='poo.proiect@gmail.com',
            recipients=[booking.email]
        )
        msg.body = f"Thank you for your booking!\n\nMovie: {movie.title}\nSeats: {booking.seats}\nBooking ID: {booking.id}\n\nPlease find your QR code attached."
        msg.attach('ticket_qr.png', 'image/png', qr_bytes)
        mail.send(msg)

        return jsonify({'message': 'Booking successful!', 'booking_id': booking.id}), 201
    else:
        return jsonify({'message': 'Payment failed. Please try again.'}), 400

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