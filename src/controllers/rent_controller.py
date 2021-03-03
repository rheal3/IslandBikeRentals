from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from sqlalchemy import exists

rent = Blueprint("rent", __name__, url_prefix="/rent")

# redirect from "/rent" to "/rent/payment" to "/rent/success"

def total_due(rt, ct, np):
    time = int(rt[:2]) - int(ct[:2])
    if time == 1:
        return str(20 * int(np))
    elif time == 2:
        return str(30 * int(np))
    elif time == 3:
        return str(40 * int(np))
    else:
        return str(70 * int(np))



@rent.route("/", methods=["POST", "GET"])
def booking_create():
    """
    Create a new booking.
    """
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        num_participants = request.form.get("num_participants")
        month = request.form.get("month")
        day = request.form.get("day")
        year = request.form.get("year")
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

        amt_due = total_due(return_time, collection_time, num_participants) 

        return redirect(url_for("rent.booking_payment", amt_due=amt_due, id=new_booking.id))
    return render_template("rental_form.html")

@rent.route("/payment", methods=["POST", "GET"])
def booking_payment():
    amt_due = request.args.get("amt_due")
    id = request.args.get("id")
    booking = Booking.query.get(id)

    if request.method == "POST":
        new_payment = Payment()
        new_payment.full_amount_due = float(request.form.get("full_amount_due"))
        new_payment.upfront_amount_paid = request.form.get("upfront_amount_paid")
        
        if new_payment.upfront_amount_paid == "full":
            new_payment.remainder_due = 0
        elif new_payment.upfront_amount_paid == "deposit":
            new_payment.remainder_due = new_payment.full_amount_due - 50
        
        new_payment.booking_id = request.form.get("booking_id")
        
        (ret, ),  = db.session.query(exists().where(Payment.booking_id==new_payment.booking_id))
        if not ret:
            db.session.add(new_payment)
            db.session.commit()

        return redirect(url_for("rent.booking_success"))

    return render_template("payment_form.html", amt_due=amt_due, id=id, booking=booking)

@rent.route("/success", methods=["GET"])
def booking_success():
    booking = Booking.query.order_by(Booking.id.desc()).first()
    payment = Payment.query.filter_by(id=booking.id).first()
    return render_template("rent_success.html", booking=booking, payment=payment)
