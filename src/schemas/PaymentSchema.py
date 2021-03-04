from main import ma
from models.Payment import Payment


class PaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payment


payment_schema = PaymentSchema()
payments_schema = PaymentSchema(many=True)
