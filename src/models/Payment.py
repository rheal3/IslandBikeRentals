from main import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    full_amount_due = db.Column(db.Integer, nullable=False)
    upfront_amount_paid = db.Column(db.String, nullable=False)
    remainder_due = db.Column(db.Integer, nullable=False)

    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"),
                           nullable=False)
