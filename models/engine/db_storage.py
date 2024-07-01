#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import Basemodel, Base
import os
from os import getenv
import models
import sqlalchemy
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

"""DBStorage class for interacting with MySQL database"""

def __init__(self):
    """Initialize the MySQL Database Storage """
    db_name = getenv('HBNH_MYSQL_DB')
    host = getenv('HBNH_MYSQL_HOST', 'localhost')
    password = getenv('HBNH_MYSQL_PWD')
    username = getenv('HBNH_MYSQL_USER', 'hbnb_user')
    connection = f'mysql+mysqldb://{username}:{password}@{host}/{db_name}'


class DBStorage:
    """what do"""
    __engine = None
    __session = None
    __file_storagee = FileStorage()
    
    
    def __init__(self):
        """Make obj and conncet to db"""
        self.__engine = create_engine(connection)

    def all(self, cls=None):
        """Query all objects from the database"""
        objects = {}
        if cls:
            #If class is specified, all objects of that class are queried
            query_results = self.__session.query(classes[cls]).all()
            for objects in query_results:
                key = f"{cls.__name__}.{obj.id}"
                objects[key] = obj
        else:
            #If no class is specified, objects of all classes are queried
            query_result = []
            for model_class in classes.values():
                query_result = (self.__session.query(model_class).all())
                for obj in query_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
                return objects
                                
    def new(self, obj):
        """Add the object to the database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the database"""
        if obj is None:
            return self.__session.delete(obj)

    def reload(self):
        """Create all tables in database"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    @property
    def file_storage(self):
        """Getter for file storage"""
        return self.__file_storagee
    
    def close(self):
        """Close the database session"""
        self.__session.close()
