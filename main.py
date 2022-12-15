from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"


app.run(host="0.0.0.0", port=5001)