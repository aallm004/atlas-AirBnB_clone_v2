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
    # Load cities (assuming state_id is 1 for example)
    cities = load_cities(1)  # Replace with the actual state ID

    # Sort cities by name
    sorted_cities = sorted(cities, key=lambda city: city.name)

    # Render the template with the sorted cities
    return render_template('10-hbnb_filters.html', cities=sorted_cities)

@app.teardown_appcontext
def close_db_session(exception=None):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
