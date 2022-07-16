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

@APP.route('/news', methods=["GET"])
def get_news():
    search = request.args.get("search")
    return requests.get(f"{news['base_url']}/v2/everything?apiKey={news['api_key']}&q={search}").json()

@APP.route('/news/headlines', methods=["GET"])
def get_news_headlines():
    search = request.args.get("search")
    category = request.args.get("category")
    country = request.args.get("country")
    query_string = ""
    
    if search:
        query_string += f"&q={search}"
    if category:
        query_string += f"&category={category}"
    if country:
        query_string += f"&country={country}"
    # print(f"{query_string=}")
    return requests.get(f"{news['base_url']}/v2/top-headlines?apiKey={news['api_key']}{query_string}").json()

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

APP.run(host="0.0.0.0", debug=True, port=8080)
