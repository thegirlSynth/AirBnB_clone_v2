#!/usr/bin/python3
"""This script starts a Flask web application."""

from flask import Flask, render_template


webapp = Flask(__name__)


@webapp.route('/', strict_slashes=False)
def say_hello():
    return 'Hello HBNB!'


@webapp.route('/hbnb', strict_slashes=False)
def say_HBNB():
    return 'HBNB'


@webapp.route('/c/<text>', strict_slashes=False)
def replace_C(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@webapp.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@webapp.route('/python/<text>', strict_slashes=False)
def replace_Python(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@webapp.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    return '{} is a number'.format(n)


@webapp.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    return render_template('5-number.html', n=n)


@webapp.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n=None):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    webapp.run(host='0.0.0.0', port=5000)
