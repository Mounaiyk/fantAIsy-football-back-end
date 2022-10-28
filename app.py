from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
