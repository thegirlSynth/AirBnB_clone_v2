#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


newapp = Flask(__name__)


@newapp.teardown_appcontext
def teardown(exception=None):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


@newapp.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    newapp.run(host="0.0.0.0", port=5000)
