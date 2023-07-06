from flask import Flask
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
