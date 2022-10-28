from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
import requests

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/stats')
def get_all_stats():
    resp = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    data = resp.json()
    return data["elements"]

@app.route('/login' methods=['POST'])
def



if __name__ == "__main__":
    app.run(debug=True)
