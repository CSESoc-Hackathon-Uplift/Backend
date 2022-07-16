from flask import Flask

app = Flask(__name__)

@app.route('/get_news', methods=["POST"])
def get_news():
    body = request.get_json()
    
