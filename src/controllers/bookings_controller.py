from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
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

@bookings.route("/<int:id>", methods=["POST", "GET"])
def booking_show(id):
    """
    Show data for single booking using id.
    """
    booking = Booking.query.get(id)
    payment = Payment.query.filter_by(booking_id=id).first()
    return render_template("bookings_single.html", booking=booking, payment=payment)

@bookings.route("/<int:id>/delete", methods=["GET", "DELETE"])
def booking_delete(id):
    """
    Delete data for single booking using id.
    """
    booking = Booking.query.get(id)
    payment = Payment.query.filter_by(booking_id=id).first()
    if not booking:
        return "DELETED"
    db.session.delete(booking)
    db.session.delete(payment)
    db.session.commit()
    return redirect(url_for('bookings.booking_index'))

@bookings.route("/<int:id>/update", methods=["POST", "GET"])
def booking_update(id):
    """
    Update booking using id.
    """
    if request.method == "POST":
        month = request.form.get("month")
        day = request.form.get("day")
        year = request.form.get("year")

        booking = Booking.query.filter_by(id=id).first()
        booking.first_name = request.form.get("first_name")
        booking.last_name = request.form.get("last_name")
        booking.phone = request.form.get("phone")
        booking.email = request.form.get("email")
        booking.num_participants = request.form.get("num_participants")
        booking.booking_date = f"{year}-{month}-{day}"
        booking.collection_time = request.form.get("collection_time")
        booking.return_time = request.form.get("return_time")

        if request.form.get("rental_complete") == True:
            booking.rental_complete = True
        else:
            booking.rental_complete = False

        payment = Payment.query.filter_by(booking_id=id).first()
        payment.full_amount_due = float(request.form.get("full_amount_due"))

        if request.form.get("remainder_due_check") == "paid":
            payment.remainder_due = 0
        else:
            payment.remainder_due = request.form.get("remainder_due")

        db.session.commit()

        return redirect(url_for("bookings.booking_index"))

    booking = Booking.query.get(id)
    payment = Payment.query.filter_by(booking_id=id).first()
    return render_template("booking_update.html", booking=booking, payment=payment)
