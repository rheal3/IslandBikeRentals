from flask import Blueprint, request, jsonify, render_template

home = Blueprint("home", __name__, url_prefix="/")

@home.route("/", methods=["GET"])
def home_page():
    """
    Returns simple home page.
    """
    return render_template("home_page.html")
