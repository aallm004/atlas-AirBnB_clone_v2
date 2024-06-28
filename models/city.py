#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
