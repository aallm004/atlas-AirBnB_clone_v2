#!/usr/bin/python3
""" Place Module for HBNB project """
# Imports necessary SQLAlchemy classes for defining db schema and data types.
from os import getenv
from sqlalchemy import (Column, String, ForeignKey, float, Integer, Table)
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.review import Review

association_table = Table('place_amenity', Base.metadata)


class Place(BaseModel, Base):
    """ A place to stay """
    # Defines name of table in the database that will store Place records.
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(float)
    longitude = Column(float)
    reviews = relationship('Review', backref='place',
                           cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenities', viewonly=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """
            commentary
            """
            all_reviews = list(models.storage.all(Review).values())
            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list
