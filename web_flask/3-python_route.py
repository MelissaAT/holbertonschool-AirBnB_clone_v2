#!/usr/bin/python3
"""Write a script that starts a
Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_text():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    return "C %s" % text.replace('_', ' ')


@app.route("/python/", strict_slashes=False, defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return "Python " + f'{text}'.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
