from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/login")
def login():
    return render_template("login.html", title="Log in")


@main.route("/")
def home():
    return render_template("home.html", title="Home")
