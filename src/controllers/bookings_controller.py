from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template
from sqlalchemy.orm import joinedload


bookings = Blueprint("bookings", __name__, url_prefix="/bookings")

@bookings.route("/", methods=["GET"])
def booking_index():
    """
    Returns index of all bookings.
    """
    bookings = Booking.query.order_by(Booking.booking_date.asc()).all()
    payments = Payment.query.all()
    return render_template("bookings_index.html", bookings=bookings, payments=payments)    

@bookings.route("/<int:id>", methods=["GET"])
def booking_show(id):
    """
    Show data for single booking using id.
    """
    booking = Booking.query.get(id)
    payment = Payment.query.filter_by(booking_id=id).first()
    # return jsonify(booking_schema.dump(booking))
    return render_template("bookings_single.html", booking=booking, payment=payment)

@bookings.route("/delete/<int:id>", methods=["DELETE"])
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

@bookings.route("/update/<int:id>", methods=["POST", "GET"])
def booking_update(id):
    """
    Update booking using id.
    """
    pass

    # if request.method == "POST":
    #     booking = Booking.query.filter_by(id=id)
    #     booking_fields = booking_schema.load(request.json)
    #     booking.update(booking_fields)
    #     db.session.commit()
        # return jsonify(booking_schema.dump(booking[0]))
        # return template
    # return template
