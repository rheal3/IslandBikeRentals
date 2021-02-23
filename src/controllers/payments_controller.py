from models.Payment import Payment
from schemas.PaymentSchema import payment_schema, payments_schema
from main import db
from flask import Blueprint, request, jsonify, render_template
from sqlalchemy.orm import joinedload


payments = Blueprint("payments", __name__, url_prefix="/payments")



@payments.route("/<int:id>", methods=["GET"])
def payment_show(id):
    """
    Show data for single booking using id.
    """
    payment = Payment.query.get(id)
    # return jsonify(payment_schema.dump(payment))
    return render_template("payment_show.html", payment=payment)

