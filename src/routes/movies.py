from flask import Blueprint, render_template, request, redirect, url_for
from src.models.movie import Movie
from src.extensions import db

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies')
def movie_listings():
    movies = Movie.query.all()
    return render_template('movie_listings.html', movies=movies)

@movies_bp.route('/movies/<int:movie_id>')
def movie_details(movie_id):
    movie = Movie.query.get(movie_id)
    return render_template('movie_details.html', movie=movie)