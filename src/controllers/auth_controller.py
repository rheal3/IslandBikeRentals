from models.User import User
from main import db
from flask import Blueprint, request, abort, render_template, redirect, url_for
from main import bcrypt
from flask_login import login_user, logout_user, login_required
# from datetime import timedelta

auth = Blueprint('auth', __name__)


@auth.route("/", methods=["GET"])
def home_page():
    """
    Returns simple home page.
    """
    return render_template("home_page.html")


@auth.route("/auth/register", methods=["POST"])
def auth_register():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user:
        return abort(400, description="user already exists")
    user = User()

    user.username = username
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route("/auth/login", methods=["POST"])
def auth_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    # don't login if the user doesn't exist
    if not user:
        return abort(401, description="Incorrect username")
    if not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Incorrect password")

    login_user(user)
    return redirect(url_for('bookings.booking_index'))


@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home_page'))

# @auth.route("/users", methods=["GET"])
# def users_index():
#     users = User.query.all()
#     return jsonify(users_schema.dump(users))
