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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
