import smtplib
import ssl
import os


def send_email(booking, payment):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("IBR_EMAIL")
    recipient_email = booking.email
    password = os.getenv("IBR_EMAIL_PASSWORD")
    message = f"""\
Subject: Island Bike Rentals Receipt

This is your receipt from IBR your booking details are as follows:

REFERENCE: #{booking.id}
PERSONAL DETAILS
    Name: {booking.first_name} {booking.last_name}
    Phone: {booking.phone}
    Email: {booking.email}

BOOKING DETAILS
    Num. Participants: {booking.num_participants}
    Date: {booking.booking_date}
    Collection Time: {booking.collection_time}
    Return Time: {booking.return_time}

PAYMENT DETAILS
    Full Amount Due: ${payment.full_amount_due}.00
    Upfront Amount Paid: {payment.upfront_amount_paid}
    Remainder Due: ${payment.remainder_due}.00

Bye"""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message)
