#!/usr/bin/python3
"""test_amenity"""
import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test the class Amenity"""

    def test_amenity(self):
        """Test the initialization of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "name"))
