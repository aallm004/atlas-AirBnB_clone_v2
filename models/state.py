#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.city import City
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if storage_type != "db":
        @property
        def cities(self):
            """Getter attribute for cities."""
            from models import City, storage
            listofcities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    listofcities.append(city)
                    return listofcities
