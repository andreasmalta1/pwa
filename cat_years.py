from flask import Blueprint, render_template, request
import random

cat_years = Blueprint("cat_years", __name__)


@cat_years.route("/", methods=["GET", "POST"])
def get_cat_years():
    if request.method == "POST":
        cat_years = request.form["cat-years"]
        if request.form["convert"] == "get-human":
            human_years = convert_to_human(int(cat_years))

        return render_template("cat.html", cat_years=cat_years, human_years=human_years)

    if request.method == "GET":
        return render_template("cat.html")


def convert_to_human(years):
    if years == 1:
        return 15

    if years == 2:
        return 24

    return ((years - 2) * 4) + 24
