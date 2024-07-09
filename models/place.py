#!/usr/bin/python3
""" Place Module for HBNB project """
# Imports necessary SQLAlchemy classes for defining db schema and data types.
from os import getenv
from sqlalchemy import (Column, String, ForeignKey, Float, Integer, Table)
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base, storage_type
import models
from models.review import Review
from models.amenity import Amenity

if storage_type == "db":
    association_table = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    # Defines name of table in the database that will store Place records.
    __tablename__ = 'places'

    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')

        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False)
        amenity_ids = []

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        review_ids = []
        amenities = []
        reviews = []

        @property
        def reviews(self):
            """
            commentary
            """
            all_reviews = list(models.storage.all(Review).values())
            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list

        @property
        def amenities(self):
            """
            Returns list of Amenity instances based on attribute amenity_ids.
            """
            all_amenities = list(models.storage.all(Amenity).values())
            amenity_list = [a for a in all_amenities if
                            a.id in self.amenity_ids]
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Adds an Amenity.id to the amenity_id attribute."""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
            else:
                # Optionally, log a warning or handle invalid input as needed
                pass
