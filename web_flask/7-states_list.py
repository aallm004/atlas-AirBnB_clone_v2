#!/usr/bin/python3
"Script that begins a flask webappppp"
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_states():
    """Display a list of State objects sorted by name."""
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('states_list.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
