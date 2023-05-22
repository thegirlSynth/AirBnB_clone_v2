#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask


webapp = Flask(__name__)


@webapp.route('/', strict_slashes=False)
def say_hello():
    return 'Hello HBNB!'

@webapp.route('/hbnb', strict_slashes=False)
def say_HBNB():
    return 'HBNB!'


if __name__ == '__main__':
    webapp.run(host='0.0.0.0', port=5000)
