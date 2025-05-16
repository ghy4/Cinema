from src.extensions import db, Base

class Booking(Base):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    booking_time = db.Column(db.DateTime, nullable=False)
    user = db.relationship('User', backref='bookings')
    movie = db.relationship('Movie', backref='bookings')
    def __repr__(self):
        return f'<Booking {self.id}>'