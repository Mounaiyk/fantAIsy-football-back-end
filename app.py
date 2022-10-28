from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///player_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

with app.app_context():
    db.create_all()

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/stats')
def get_all_stats():
    resp = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    data = resp.json()
    return data["elements"]

# @app.route('/login' methods=['POST'])
# def



if __name__ == "__main__":
    app.run(debug=True)
