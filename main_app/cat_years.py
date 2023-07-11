from flask import Blueprint, render_template, request
import random

cat_years = Blueprint("cat_years", __name__)


@cat_years.route("/", methods=["GET", "POST"])
def get_cat_years():
    if request.method == "POST":
        cat_years = request.form["cat-years"]
        human_years = request.form["human-years"]
        # if request.form.get("get_human"):
        #     print("Converting to human")
        # if request.form.get("get_cat"):
        #     print("Converting to cat years")
        # ^^ NOT WORKING

        # https://stackoverflow.com/questions/19794695/flask-python-buttons

        return render_template("cat.html", cat_years=cat_years, human_years=human_years)

    if request.method == "GET":
        return render_template("cat.html")
