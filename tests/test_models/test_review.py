#!/usr/bin/python3
"""test_review"""
import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test the class Review"""

    def test_init(self):
        """unit tests for Review"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
