from flask import render_template, Blueprint
from pmo_sys import Flask

main = Blueprint("main", __name__)


@main.route("/login")
def login():
    return render_template("login.html", title="Log in")


@main.route("/")
def dashboard():
    return render_template("dashboard.html", title="Home")


@main.route("/project")
def projects():
    return render_template("projects.html", title="Projects")


@main.route("/forms")
def forms():
    return render_template("forms.html", title="Forms")


@main.route("/dev")
def dev():
    return render_template("dev.html", title="dev")
