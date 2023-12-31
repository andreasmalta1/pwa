from flask import Blueprint, render_template, request
import random

randomize = Blueprint("random", __name__)


@randomize.route("/color", methods=["GET", "POST"])
def get_random_color():
    if request.method == "POST":
        r = lambda: random.randint(0, 255)
        color = "#%02X%02X%02X" % (r(), r(), r())
        return render_template("color.html", color=color)

    if request.method == "GET":
        return render_template("color.html")


@randomize.route("/picker", methods=["GET", "POST"])
def get_random_text():
    if request.method == "POST":
        text = request.form["text"]
        text_list = text.split("\n")
        random_text = random.choice(text_list)
        return render_template("text.html", input_text=text, random_text=random_text)

    if request.method == "GET":
        return render_template("text.html")
