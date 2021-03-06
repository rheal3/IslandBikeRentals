from main import db


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    num_participants = db.Column(db.Integer, nullable=False)
    booking_date = db.Column(db.String, nullable=False)
    collection_time = db.Column(db.String, nullable=False)
    return_time = db.Column(db.String, nullable=False)
    rental_complete = db.Column(db.Boolean, default=False)

    payment = db.relationship("Payment", backref="booking",
                              cascade="all, delete")
