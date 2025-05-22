from src.extensions import db, Base

class Movie(Base):
    __tablename__ = 'movies'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    duration = db.Column(db.Integer)
    poster_url = db.Column(db.String)
    release_date = db.Column(db.Date, nullable=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinemas.id'))
    cinema = db.relationship('Cinema', back_populates='movies')

    def __repr__(self):
        return f'<Movie {self.title}>'