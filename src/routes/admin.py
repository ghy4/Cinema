from flask import Blueprint, render_template, request, redirect, url_for, flash
from urllib.parse import urlparse
from src.models.movie import Movie
from src.models.user import User, Employee, Manager
from src.models.booking import Booking
from src.extensions import db
from utils.decorators import roles_required_oop


admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
@roles_required_oop(Manager)
def dashboard():
    return render_template('admin_dashboard.html')

@admin_bp.route('/admin/movies')
@roles_required_oop(Manager)
def manage_movies():
    movies = Movie.query.all()
    return render_template('manage_movies.html', movies=movies)

@admin_bp.route('/admin/movies/add', methods=['GET', 'POST'])
@roles_required_oop(Manager)
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        duration = request.form['duration']
        rating = request.form['rating']
        poster_url = request.form['poster_url']
        parsed_url = urlparse(poster_url)
        if not (parsed_url.scheme in ['http', 'https'] and parsed_url.netloc):
            flash('Please provide a valid external image URL (starting with http or https).', 'danger')
            return render_template('add_movie.html')
        new_movie = Movie(title=title, genre=genre, duration=duration, rating=rating, poster_url=poster_url)
        db.session.add(new_movie)
        db.session.commit()
        flash('Movie added successfully!', 'success')
        return redirect(url_for('admin.manage_movies'))
    return render_template('add_movie.html')

@admin_bp.route('/admin/movies/edit/<int:movie_id>', methods=['GET', 'POST'])
@roles_required_oop(Manager)
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        movie.title = request.form['title']
        movie.genre = request.form['genre']
        movie.duration = request.form['duration']
        movie.rating = request.form['rating']
        poster_url = request.form['poster_url']
        parsed_url = urlparse(poster_url)
        if not (parsed_url.scheme in ['http', 'https'] and parsed_url.netloc):
            flash('Please provide a valid external image URL (starting with http or https).', 'danger')
            return render_template('edit_movie.html', movie=movie)
        movie.poster_url = poster_url
        db.session.commit()
        flash('Movie updated successfully!', 'success')
        return redirect(url_for('admin.manage_movies'))
    return render_template('edit_movie.html', movie=movie)

@admin_bp.route('/admin/movies/delete/<int:movie_id>', methods=['POST'])
@roles_required_oop(Manager)
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('Movie deleted successfully!', 'success')
    return redirect(url_for('admin.manage_movies'))

@admin_bp.route('/admin/users')
@roles_required_oop(Manager)
def manage_users():
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@admin_bp.route('/admin/users/delete/<int:user_id>', methods=['POST'])
@roles_required_oop(Manager)
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('admin.manage_users'))

@admin_bp.route('/admin/bookings')
@roles_required_oop(Manager)
def manage_bookings():
    bookings = Booking.query.all()
    return render_template('manage_bookings.html', bookings=bookings)