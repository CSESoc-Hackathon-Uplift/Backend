from flask import Flask, request
from history import History
import json
import requests
APP = Flask(__name__)

with open("news.json") as f:
    news = json.load(f)

@APP.route("/", methods=["GET"])
def root():
    return "<h1 style='font-family: Arial'; font-size: 60px;'>Welcome to Uplift's backend API!</h1>"

