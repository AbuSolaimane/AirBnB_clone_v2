#!/usr/bin/python3
"""
this is a module
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """this a function"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this a function"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def descripe_c(text):
    """this a function"""
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def descripe_python(text="is cool"):
    """this a function"""
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
