import unittest
import os
from models.Booking import Booking
from models.Payment import Payment
from main import create_app, db

class TestBookings(unittest.TestCase):
    @classmethod
    def setUp(cls):
        if os.environ.get("FLASK_ENV") != "testing":
            raise EnvironmentError("FLASK_ENV is not testing")
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    # test the POST method in /rent/ 
    def test_booking_create(self):
        # data for the new booking
        booking_data = {
            "first_name": "Albert", 
            "last_name": "Ramiro", 
            "phone": "4473829238", 
            "email": "dillyf@email.com",
            "num_participants": 2,
            "month": "02",
            "day": "20",
            "year": "2021",
            "collection_time": "08:00:00", 
            "return_time": "17:00:00"
        }

        # POST request w/url & booking data
        response = self.client.post("rent/", data=booking_data)
        data = response.get_json()

        #check if we now have a booking with that email in the booking table
        booking = Booking.query.filter_by(email=booking_data["email"]).first()

        # check the OK status
        self.assertEqual(response.status_code, 302)

        #test there's some data in the response
        self.assertIsNotNone(booking)

        # test html contains changed data from updated booking
        self.assertEqual(booking_data["first_name"], booking.first_name)
        self.assertEqual(booking_data["last_name"], booking.last_name)
        self.assertEqual(booking_data["phone"], booking.phone)
        self.assertEqual("2021-02-20", booking.booking_date)

    # test the POST method in /rent/ 
    def test_booking_payment(self):
        # create booking
        booking_data = {
            "first_name": "Albert", 
            "last_name": "Ramiro", 
            "phone": "4473829238", 
            "email": "dillyf@email.com",
            "num_participants": 2,
            "month": "02",
            "day": "20",
            "year": "2021",
            "collection_time": "08:00:00", 
            "return_time": "17:00:00"
        }
        response = self.client.post("rent/", data=booking_data)
        booking_id = Booking.query.filter_by(email=booking_data["email"]).first().id
        
        # data for new payment
        payment_data = {
            "full_amount_due": 140,
            "upfront_amount_paid": "deposit",
            "remainder_due": 90,
            "booking_id": booking_id
        }

        # POST request w/url & payment data
        response = self.client.post("rent/payment", data=payment_data)
        data = response.get_json()

        # check if new payment is in the payment table
        payment = Payment.query.filter_by(booking_id=booking_id).first()

        # check the OK status
        self.assertEqual(response.status_code, 302)

        #test there's some data in the response
        self.assertIsNotNone(payment)

        # test html contains changed data from updated booking
        self.assertEqual(payment_data["full_amount_due"], payment.full_amount_due)
        self.assertEqual(payment_data["upfront_amount_paid"], payment.upfront_amount_paid)
        self.assertEqual(payment_data["remainder_due"], payment.remainder_due)
        self.assertEqual(payment_data["booking_id"], payment.booking_id)

