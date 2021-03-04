from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version cascade;")
    print("Tables deleted")


@db_commands.cli.command("seed")
def seed_db():
    from models.Booking import Booking
    from models.Payment import Payment
    from models.User import User
    from main import bcrypt

    u1 = User()
    u1.username = "admin"
    u1.password = bcrypt.generate_password_hash("nimda").decode("utf-8")
    db.session.add(u1)
    db.session.commit()

    b1 = Booking()
    b1.first_name = "a"
    b1.last_name = "a"
    b1.phone = "123456789"
    b1.email = "aa@email.com"
    b1.num_participants = 3
    b1.booking_date = "2021-03-20"
    b1.collection_time = "08:00"
    b1.return_time = "17:00"

    db.session.add(b1)

    b2 = Booking()
    b2.first_name = "b"
    b2.last_name = "b"
    b2.phone = "987654321"
    b2.email = "bb@email.com"
    b2.num_participants = 2
    b2.booking_date = "2021-03-21"
    b2.collection_time = "10:00"
    b2.return_time = "15:00"

    db.session.add(b2)

    db.session.commit()

    p1 = Payment()
    p1.full_amount_due = 210.00
    p1.upfront_amount_paid = "deposit"
    p1.remainder_due = 160.00
    p1.booking_id = 1

    db.session.add(p1)

    p2 = Payment()
    p2.full_amount_due = 140.00
    p2.upfront_amount_paid = "full"
    p2.remainder_due = 0.00
    p2.booking_id = 2

    db.session.add(p2)

    db.session.commit()

    print("Tables seeded")
