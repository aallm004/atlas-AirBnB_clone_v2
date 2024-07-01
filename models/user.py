#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    # Defines the name of the table in the database that will store User record
        __tablename__ = 'users'
        # represents a column containing a string (128 characters); cant be null
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        # Defines a relationship between User model and the Place model
        # The 'places' attribute will store a list of Place objects associated
        # with this User.
        # The 'backref' attribute ensures that each Place object will have a
        # reference to its User via the 'User' attribute.
        # The 'cascade' attribute ensures that all Place objects linked to a
        # User will be automatically deleted if the User is deleted.
        places = relationship('Place', backref='user',
                               cascade='all, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete-orphan')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
