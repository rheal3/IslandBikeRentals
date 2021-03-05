from controllers.auth_controller import auth
from controllers.bookings_controller import bookings
from controllers.rent_controller import rent

registerable_controllers = [
    auth,
    bookings,
    rent
]
