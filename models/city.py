#!/usr/bin/python3
""" City Module for HBNB project """
<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey
=======
from sqlalchemy.orm import relationship # Import the relationship function from SQLAlchemy to define relationships between models
from sqlalchemy import Column, String, ForeignKey # Import needed classes from SQLAlchemy to define schema of the City model.
>>>>>>> b6e9851bb0ed8143b8eaae04274f996174bbf08f
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete-orphan")    
=======
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
>>>>>>> b6e9851bb0ed8143b8eaae04274f996174bbf08f
