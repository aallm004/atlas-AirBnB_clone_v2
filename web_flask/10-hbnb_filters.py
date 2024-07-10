#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


# Load all cities of a State
def load_cities(state_id):
    state = storage.get("State", state_id)
    if state:
        return state.cities if hasattr(state, "cities") else []


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ get the stuff """
        # Load cities (assuming state_id is 1 for example)
    from models.city import City
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda c: c.name)

    from models.state import State
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)

    from models.amenity import Amenity
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda a: a.name)

    return render_template('10-hbnb_filters.html',
                           cities=sorted_cities,
                           states=sorted_states,
                           amenities=sorted_amenities)


@app.teardown_appcontext
def close_db_session(exception=None):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
