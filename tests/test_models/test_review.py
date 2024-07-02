#!/usr/bin/python3
"""
Unit tests for Review class in models/review.py
"""
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_text(self):
        """
        Test is 'text' attribute is of type str
        """
        new = self.value(text="too many rats")
        self.assertEqual(type(new.text), str)

    def test_place_id(self):
        """
        Test is 'place_id' attribute is of type str.
        """
        new = self.value(place_id="1234")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test is 'user_id' attribute is of type str.
        """
        new = self.value(user_id="123")
        self.assertEqual(type(new.user_id), str)
    
    def test_text_not_nullable(self):
        """
        Test if 'text' attribute is non-nullable
        """
        with self.assertRaises(TypeError):
            new_review = self.value(text=None)
    
    def test_place_id_not_nullable(self):
        """
        Test if 'place_id' attribute is non-nullable
        """
        with self.assertRaises(TypeError):
            new_review = self.value(place_id=None)
        
    def test_text_max_length(self):
        """
        Test if 'text' attribute does not exceed maximum length
        """
        long_text = "a" * 1025 # Exceeds maximum length of 1024
        with self.assertRaises(ValueError):
            new_review = self.value(text=long_text)

    def test_review_place_relationship(self):
        """
        Test relationship between Review and Place
        """
        new_place = Place()
        new_review = self.value(place_id=new_place.id)
        self.assertEqual(new_review.place_id, new_place.id)
    
    def test_review_user_relationship(self):
        """
        Test relationship between Review and User
        """
        # Assuming you have a User class and relationship set up
        new_user = User()
        new_review = self.value(user_id=new_user.id)
        self.assertEqual(new_review.user_id, new_user.id)
