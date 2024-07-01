#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""

