from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload


bookings = Blueprint("bookings", __name__, url_prefix="/bookings")

@bookings.route("/", methods=["GET"])
def booking_index():
    """
    Returns index of all bookings.
    """
    # bookings = Booking.query.options(joinedload("payment")).all()
    bookings = Booking.query.all()
    # payments = Payment.query.all()
    # return jsonify(payments_schema.dump(payments))
    return jsonify(bookings_schema.dump(bookings))

@bookings.route("/", methods=["POST"])
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

    # redirect to payment "/bookings/payment" without commiting until payment confirmation
    # returns booking details and sends to booking_payment??
    

@bookings.route("/<int:id>", methods=["GET"])
def booking_show(id):
    """
    Show data for single booking using id.
    """
    booking = Booking.query.get(id)
    return jsonify(booking_schema.dump(booking))

@bookings.route("/<int:id>", methods=["DELETE"])
def booking_delete(id):
    """
    Delete data for single booking using id.
    """
    booking = Booking.query.get(id)
    if not booking:
        return "DELETED"
    db.session.delete(booking)
    db.session.commit()
    return jsonify(booking_schema.dump(booking))

@bookings.route("/<int:id>", methods=["PUT", "PATCH"])
def booking_update(id):
    """
    Update booking using id.
    """
    booking = Booking.query.filter_by(id=id)
    booking_fields = booking_schema.load(request.json)
    booking.update(booking_fields)
    db.session.commit()
    return jsonify(booking_schema.dump(booking[0]))

# redirect from "/" POST method ??
@bookings.route("/payment", methods=["POST"])
def booking_payment():
    payment_fields = payment_schema.load(request.json)

    new_payment = Payment()
    new_payment.full_amount_due = payment_fields["full_amount_due"]
    new_payment.upfront_amount_paid = payment_fields["upfront_amount_paid"]
    new_payment.remainder_due = payment_fields["remainder_due"]

    db.session.add(new_payment)
    db.session.commit()
    return jsonify(payment_schema.dump(new_payment))
