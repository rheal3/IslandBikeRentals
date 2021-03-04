import unittest
import os
from models.User import User
from main import create_app, db, bcrypt

class TestAuth(unittest.TestCase):
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

    # test the POST method in /auth/register 
    def test_register(self):
        login_data = {
            'username': 'tester',
            'password': '123456'
        }

        response = self.client.post('/auth/register', data=login_data)
        data = response.get_json()

        user = User.query.filter_by(username=login_data["username"]).first()

        # check the OK status
        self.assertEqual(response.status_code, 302)

        #test there's some data in the response
        self.assertIsNotNone(user)

        # test html contains changed data from updated booking
        self.assertEqual(login_data["username"], user.username)
        self.assertTrue(bcrypt.check_password_hash(user.password, login_data["password"]))


    # test the POST method in /auth/login 
    def test_login(self):
        login_data = {
            'username': 'tester@email.com',
            'password': '123456'
        }
        response = self.client.post('/auth/register', data=login_data)

        response = self.client.post('/auth/login', data=login_data, follow_redirects=True)
        data = response.get_json()

        # check the OK status
        self.assertEqual(response.status_code, 200)





