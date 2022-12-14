from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world!"


if "__main__" == __name__:
    app.run(port="8080")