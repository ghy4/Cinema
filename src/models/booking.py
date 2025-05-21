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
    
    @classmethod
    def get_user_bookings(self, user_id):
        return self.query.filter_by(user_id=user_id).all()
    
    @classmethod
    def get_all_bookings(cls):
        return cls.query.all()

    @classmethod
    def get_booking_by_id(cls, booking_id):
        return cls.query.get(booking_id)

    @classmethod
    def cancel_booking(self, booking_id):
        booking = self.query.get(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return True
        return False