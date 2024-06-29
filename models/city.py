#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship # Import the relationship function from SQLAlchemy to define relationships between models
from sqlalchemy import Column, String, ForeignKey # Import needed classes from SQLAlchemy to define schema of the City model.
from models.base_model import BaseModel, Base
from models.state import State

class City(BaseModel):
    """ The city class, contains state ID and name """
    # Define name of the table in the database that will store City records.
    __tablename__ = 'cities'

    # Define column for the name of the city. The name is the string of up to 128 characters and cannot be null.
    name = Column(String(128), nullable=False)
    # Define attribute for the state ID. This will be replaced with a proper column definition
    state_id = ""
    # Define relationship between the City model and the Place model.
    # 'places' attribute will store a list of Place objects associated with this City.
    # 'backref' attribute ensures that each Place object will have a reference to its City via the 'cities' attribute.
    # The 'cascade' attribute ensures that all Place objects linked to a City will be automatically deleted if the City is deleted.
    places = relationship('Place', backref='cities', cascade='all, delete-orphan')