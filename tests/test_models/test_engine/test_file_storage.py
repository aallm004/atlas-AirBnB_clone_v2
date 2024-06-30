"""test_file_storage module"""
import unittest
import os
import json
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """TestFileStorage class documentation"""
    def setUp(self):
        """ setup for all tests """
        self.model = BaseModel()
        self.storage = FileStorage()
        self.storage.save()

    def tearDown(self):
        """ teardown for all tests """
        del self.model
        del self.storage
        os.remove("file.json")

    def test_new(self):
        """test new method for file_storage"""
        file = FileStorage()
        self.assertEqual(type(file.file_path), str)
    
    def test_all(self):
        """test all method for file_storage"""
        model = BaseModel()
        my_dict = self.storage.all()
        self.assertIsInstance(my_dict, dict)
        self.assertIn(model, my_dict.values())

    def test_save(self):
        self.new_model = BaseModel()
        self.new_model.save()
        self.new = self.storage.reload()
        self.assertEqual(self.new, self.storage.reload())
    
    def test_reload(self):
        self.instance = BaseModel()
        self.storage.new(self.instance)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{self.instance.id}", self.storage.all())

if __name__ == '__main__':
    unittest.main()
