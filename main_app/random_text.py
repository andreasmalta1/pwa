from flask import Blueprint, render_template, request

random_text = Blueprint("random_text", __name__)


@random_text.route("/", methods=["GET", "POST"])
def get_random_text():
    if request.method == "POST":
        text = request.form["text"]
        text = text.split("\n")
        for t in text:
            print(t)
        return render_template("text.html")

    if request.method == "GET":
        return render_template("text.html")
