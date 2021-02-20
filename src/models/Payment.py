from main import db

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    full_amount_due = db.Column(db.Numeric(), nullable=False)
    upfront_amount_paid = db.Column(db.Numeric(), nullable=False)
    
    # card details <- should these be seperate??
    # card_name = db.Column(db.String, nullable=False)
    # card_number = db.Column(db.String, nullable=False)
    # card_cvv = db.Column(db.String, nullable=False)
    # card_date = db.Column(db.Integer, nullable=False)
    
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"), nullable=False)