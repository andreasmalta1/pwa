from flask import Blueprint, render_template, request, flash
from pyshorteners import Shortener

url = Blueprint("url", __name__)


@url.route("/", methods=["GET", "POST"])
def shorten_url():
    if request.method == "POST":
        long_url = request.form["url"]

        if not long_url:
            flash("Title is required!")

        type_tiny = Shortener()

        short_url = type_tiny.tinyurl.short(long_url)
        return render_template("url.html", short_url=short_url)

    if request.method == "GET":
        return render_template("url.html")
