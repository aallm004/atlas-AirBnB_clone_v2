#!/usr/bin/python3
"""Unit tests for City"""
import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage

my_model = City()

class TestCity(unittest.TestCase):
        """tests for Class City"""

        def test_city(self):
            """unit tests for City"""
            city = City()
            self.assertIsInstance(city.state_id, str)
            self.assertIsInstance(city.name, str)
