from flask import Blueprint, render_template, request
import random

random_text = Blueprint("random_text", __name__)


@random_text.route("/", methods=["GET", "POST"])
def get_random_text():
    if request.method == "POST":
        text = request.form["text"]
        text_list = text.split("\n")
        random_text = random.choice(text_list)
        return render_template("text.html", input_text=text, random_text=random_text)

    if request.method == "GET":
        return render_template("text.html")
