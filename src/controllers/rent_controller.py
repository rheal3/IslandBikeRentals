from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify

rent = Blueprint("rent", __name__, url_prefix="/rent")

# redirect from "/rent" to "/rent/payment" to "/rent/success"

@rent.route("/", methods=["GET"])
def test():
    return "RENTING"

@rent.route("/", methods=["POST"])
def booking_create():
    """
    Create a new booking.
    """
    booking_fields = booking_schema.load(request.json)

    new_booking = Booking()
    new_booking.first_name = booking_fields["first_name"]
    new_booking.last_name = booking_fields["last_name"]
    new_booking.phone = booking_fields["phone"]
    new_booking.email = booking_fields["email"]
    new_booking.num_participants = booking_fields["num_participants"]
    new_booking.booking_date = booking_fields["booking_date"]
    new_booking.collection_time = booking_fields["collection_time"]
    new_booking.return_time = booking_fields["return_time"]

    db.session.add(new_booking)
    db.session.commit()
    return jsonify(booking_schema.dump(new_booking))
    # return redirect(url_for("rent.booking_payment"))

@rent.route("/payment", methods=["POST"])
def booking_payment():
    payment_fields = payment_schema.load(request.json)

    new_payment = Payment()
    new_payment.full_amount_due = payment_fields["full_amount_due"]
    new_payment.upfront_amount_paid = payment_fields["upfront_amount_paid"]
    new_payment.remainder_due = payment_fields["remainder_due"]

    db.session.add(new_payment)
    db.session.commit()
    return jsonify(payment_schema.dump(new_payment))
    # return redirect(url_for("rent.booking_success"))

@rent.route("/success", methods=["GET"])
def booking_success():
    pass