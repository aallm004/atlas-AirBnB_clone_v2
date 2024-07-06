#!/usr/bin/python3
"""
Script tht starts a Flask web application
port 5000 by default
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', srict_slashes=False)
def hello_hnbn():
    return "Hello HBNB!"


@app.route('/hnbn', strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C {}".format(text.replace('_', ''))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
