#!/usr/bin/python3
from sqlalchemy import create_engine
from models.base_model import Basemodel, Base
import os
import models
from models import classes
from models.engine.file_storage import FileStorage

class DBStorage:
    """what do"""
    __engine = None
    __session = None
    __file_storagee = FileStorage()
    
    
    def __init__(self):
        """Initialize DBStorage"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                        os.environ['HBNB_MYSQL_USER'],
                                        os.environ['HBNB_MYSQL_PWD'],
                                        os.environ['HBNB_MYSQL_HOST'],
                                        os.environ['HBNB_MYSQL_DB'])
                                        pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

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
        if obj:
            self.__session.delete(obj)

    @property
    def file_storage(self):
        """Getter for file storage"""
        return self.__file_storagee
    
    def close(self):
        """Close the database session"""
        self.__session.close()
