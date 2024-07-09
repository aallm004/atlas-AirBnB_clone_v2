#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

#Determine the storage type based on the environment variable
storage_type = os.getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    # Imports DBStorage class
    from models.engine.db_storage import DBStorage
    # Creates an instance of DBStorage
    storage = DBStorage()

else:
    # Import FileStorage class
    from models.engine.file_storage import FileStorage
    # Creates an instance of FileStorage
    storage = FileStorage()

# Reload data from storage
storage.reload()
