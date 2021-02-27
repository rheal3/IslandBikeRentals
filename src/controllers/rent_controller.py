from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template, redirect, url_for

rent = Blueprint("rent", __name__, url_prefix="/rent")

# redirect from "/rent" to "/rent/payment" to "/rent/success"

@rent.route("/", methods=["POST"])
def booking_create():
    """
    Create a new booking.
    """
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    num_participants = request.form.get("num_participants")
    month = request.form.get("month")
    print(month)
    day = request.form.get("day")
    print(day)
    year = request.form.get("year")
    print(year)
    collection_time = request.form.get("collection_time")
    return_time = request.form.get("return_time")
    email = request.form.get("email")
    phone = request.form.get("phone")

    # booking_fields = booking_schema.load(request.json)

    new_booking = Booking()
    new_booking.first_name = first_name
    new_booking.last_name = last_name
    new_booking.phone = phone
    new_booking.email = email
    new_booking.num_participants = num_participants
    new_booking.booking_date = f"{year}-{month}-{day}"
    new_booking.collection_time = collection_time
    new_booking.return_time = return_time

    db.session.add(new_booking)
    db.session.commit()
    # return jsonify(booking_schema.dump(new_booking))
    return redirect(url_for("rent.new_payment"))

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
    return "SUCCESS"

@rent.route("/", methods=["GET"])
def new_booking():
    return render_template("rental_form.html")

@rent.route("/payment", methods=["GET"])
def new_payment():
    return render_template("payment_form.html")
