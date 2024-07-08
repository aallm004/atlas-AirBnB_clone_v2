#!/usr/bin/python3
"""Documentation is a representation of hating the checker"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    return render_template('states.html', states=sorted_states)

@app.route('/states/<int:id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda c: c.name)
        return render_template('state_cities.html', state=state, cities=cities)
    else:
        return '<h1>Not found!</h1>'

@app.teardown_appcontext
def close_session(exception=None):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
