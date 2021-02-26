from controllers.auth_controller import auth
from controllers.bookings_controller import bookings
from controllers.rent_controller import rent
from controllers.payments_controller import payments

registerable_controllers = [
    auth,
    bookings,
    rent,
    payments
]