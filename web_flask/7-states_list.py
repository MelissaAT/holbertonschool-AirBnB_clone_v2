#!/usr/bin/python3
"""Write a script that starts a
Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


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
    if text == "is cool":
        return "Python is cool"
    else:
        return "Python " + f'{text}'.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def n_text(n):
    if type(n) == int:
        return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_template1(n=None):
    a = ""
    if n % 2 == 0:
        a = "even"
    else:
        a = "odd"
    return render_template('6-number_odd_or_even.html', number=n, a=a)



@app.route('/states_list', strict_slashes=False)
def hello_8():
    states_dict = storage.all(State)
    return render_template('7-states_list.html', states=states_dict.values())


@app.teardown_appcontext
def s_close(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
