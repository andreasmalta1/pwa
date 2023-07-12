from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)

from main_app.url import url
from main_app.random import randomize
from main_app.cat_years import cat_years

app.register_blueprint(url, url_prefix="/shorten")
app.register_blueprint(randomize, url_prefix="/random")
app.register_blueprint(cat_years, url_prefix="/cat-years")
