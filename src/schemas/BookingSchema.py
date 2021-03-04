from main import ma
from models.Booking import Booking


class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking


booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)
