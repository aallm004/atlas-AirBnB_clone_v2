#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter attribute for cities."""
        listofcities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                list.append(city)
                return listofcities
