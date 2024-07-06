#!/usr/bin/python3
"""
start flask web application
route 1 . Returns a string
route 2 . Returns the string 'HBNB'
route 3 . Returns a string 'C' followed by the value of the text variable
route 4 . Returns a string 'Python' followed by the value of the text variable
 """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
