from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)

from main_app.url import url
# from main_app.random_color import random_color
# from main_app.random_text import random_text

app.register_blueprint(url, url_prefix="/shorten")
# app.register_blueprint(random_color, url_prefix="/random-color")
# app.register_blueprint(random_text, url_prefix="/random-picker")