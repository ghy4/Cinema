from src.extensions import db, Base

class Cinema(Base):
    __tablename__ = 'cinemas'

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, index=True)
    location = db.Column(db.String)
    total_screens = db.Column(db.Integer)
    contact_number = db.Column(db.String)

    movies = db.relationship("Movie", back_populates="cinema")

    def __repr__(self):
        return f"<Cinema(name={self.name}, location={self.location})>"