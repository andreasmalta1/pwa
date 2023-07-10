from flask import Blueprint, render_template, request
import random

random_color = Blueprint("random_color", __name__)


@random_color.route("/", methods=["GET", "POST"])
def get_random_color():
    if request.method == "POST":
        r = lambda: random.randint(0, 255)
        color = "#%02X%02X%02X" % (r(), r(), r())
        return render_template("color.html", color=color)

    if request.method == "GET":
        return render_template("color.html")
