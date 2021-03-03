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

    # test the GET method in /bookings/ returns all the bookings
    def test_bookings_index(self):
        # create user & login
        response = self.client.post('/auth/register', data={
            'username': 'tester@email.com',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/auth/login', data={
            'username': 'tester@email.com',
            'password': '123456'
        }, follow_redirects=True)
        
        response = self.client.get("/bookings/")
        data = response.get_json()
        bookings = Booking.query.all()
        payments = Payment.query.all()

        # check the OK status
        self.assertEqual(response.status_code, 200)

        # test html contains data from database
        self.assertIn(bookings[0].email, str(response.data))
        self.assertIn(bookings[1].email, str(response.data))
        self.assertIn(bookings[0].booking_date, str(response.data))
        self.assertIn(bookings[1].booking_date, str(response.data))
        self.assertIn(str(payments[0].full_amount_due), str(response.data))
        self.assertIn(str(payments[1].full_amount_due), str(response.data))
        
    # test the GET method in /bookings/<int:id> returns booking data
    def test_booking_show(self):
        # create user & login
        response = self.client.post('/auth/register', data={
            'username': 'tester@email.com',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/auth/login', data={
            'username': 'tester@email.com',
            'password': '123456'
        }, follow_redirects=True)

        #get the first booking from the db -> id=1
        booking = Booking.query.first()
        payment = Payment.query.filter_by(booking_id=booking.id).first()
        response = self.client.get(f"/bookings/{booking.id}")
        data = response.get_json()

        # check the OK status
        self.assertEqual(response.status_code, 200)

        # test html contains data from database
        self.assertIn(str(booking.id), str(response.data))
        self.assertIn(booking.email, str(response.data))
        self.assertIn(booking.booking_date, str(response.data))
        self.assertIn(str(booking.num_participants), str(response.data))
        self.assertIn(str(payment.full_amount_due), str(response.data))
        self.assertIn(payment.upfront_amount_paid, str(response.data))
        self.assertIn(str(payment.remainder_due), str(response.data))
        



    # test POST method /bookings/<int:id>/update --> update booking
    def test_booking_update(self):
        # create user & login
        response = self.client.post('/auth/register', data={
            'username': 'tester@email.com',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/auth/login', data={
            'username': 'tester@email.com',
            'password': '123456'
        }, follow_redirects=True)

        # data for the updated booking
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
            "return_time": "17:00:00",
            "full_amount_due": 140,
            "upfront_amount_paid": "deposit",
            "remainder_due": 90,
            "booking_id": 1
        }

        # get the first booking from the db to update -> id=1
        booking = Booking.query.first()
        payment = Payment.query.filter_by(booking_id=booking.id).first()
        # POST request w/url & booking data
        response = self.client.post(f"/bookings/{booking.id}/update", data=booking_data)
        data = response.get_json()

         # check the OK status
        # self.assertEqual(response.status_code, 200)

        # test html contains changed data from updated booking
        self.assertEqual(booking.first_name, booking_data["first_name"])
        self.assertEqual(booking.last_name, booking_data["last_name"])
        self.assertEqual(booking.phone, booking_data["phone"])
        self.assertEqual(booking.booking_date, "2021-02-20")


    # test DELETE method /bookings/<int:id>/delete --> delete booking
    def test_booking_delete(self):
        # create user & login
        response = self.client.post('/auth/register', data={
            'username': 'tester@email.com',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 302)
        response = self.client.post('/auth/login', data={
            'username': 'tester@email.com',
            'password': '123456'
        }, follow_redirects=True)

        booking = Booking.query.first()
        payment = Payment.query.filter_by(booking_id=booking.id).first()
        response = self.client.get(f"/bookings/{booking.id}/delete")

        # # test the OK status
        # self.assertEqual(response.status_code, 200)

        # query deleted booking
        deleted_booking = Booking.query.get(booking.id)
        #test that none has been received
        self.assertIsNone(deleted_booking)


