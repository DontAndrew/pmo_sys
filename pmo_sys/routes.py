from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def hello():
    return render_template("layout.html")