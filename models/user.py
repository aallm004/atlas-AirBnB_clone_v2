#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users' # represents table name, users
    email = Column(String(128), nullable=False) # represents a column containing a string (128 characters); cant be null
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
