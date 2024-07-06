#!/usr/bin/python3
"""
start flas web application
route 1 . Returns a string
route 2 . Returns the string 'HBNB'
route 3 . Returns a string 'C' followed by the value of the text variable
route 4 . Returns a string 'Python' followed by the value of the text variable
route 5 . Returns a formatted string with the value of n
route 6 . Displays an HTML page that contains a heading and a paragraph
route 7 .
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n: int):
    num_type = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
