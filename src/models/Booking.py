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

    # payment = db.Column(db.Integer, db.ForeignKey("payments.id"))
