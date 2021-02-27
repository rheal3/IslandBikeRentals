from models.Booking import Booking
from models.Payment import Payment
from schemas.BookingSchema import booking_schema, bookings_schema
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template, redirect, url_for

rent = Blueprint("rent", __name__, url_prefix="/rent")

# redirect from "/rent" to "/rent/payment" to "/rent/success"

def total_due(rt, ct):
    time = int(rt[:2]) - int(ct[:2])
    print(time)
    if time == 1:
        return "20.00"
    elif time == 2:
        return "30.00"
    elif time == 3:
        return "40.00"
    else:
        return "70.00"



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

        db.session.add(new_booking)
        db.session.commit()

        amt_due = total_due(return_time, collection_time)

        return redirect(url_for("rent.booking_payment", amt_due=amt_due, id=new_booking.id))
    return render_template("rental_form.html")

@rent.route("/payment", methods=["POST", "GET"])
def booking_payment():
    if request.method == "POST":

        # payment_fields = payment_schema.load(request.json)

        new_payment = Payment()
        new_payment.full_amount_due = float(request.form.get("full_amount_due"))
        new_payment.upfront_amount_paid = "full"
        new_payment.remainder_due = 0
        new_payment.booking_id = request.form.get("booking_id")
        db.session.add(new_payment)
        db.session.commit()
        # return jsonify(payment_schema.dump(new_payment))
        return redirect(url_for("rent.booking_success"))
    amt_due = request.args.get("amt_due")
    id = request.args.get("id")
    return render_template("payment_form.html", amt_due=amt_due, id=id)

@rent.route("/success", methods=["GET"])
def booking_success():
    return "SUCCESS"
