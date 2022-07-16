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

@APP.route('/history/add', methods=["POST"])
def history_add():
    history = History("database.json")
    body = request.json()
    return history.add(body["uuid"], body["title"], body["source"], body["score"], body["author"], body["date_added"])

@APP.route('/history', methods=["GET"])
def history():
    uuid = request.args.get("uuid")
    history = History("database.json")
    return {
        "history": history.visited(uuid)
    }
