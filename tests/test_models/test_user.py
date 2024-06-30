#!/usr/bin/python3
"""test_user"""
import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test the class User"""

    def test_init(self):
        """Unit tests for User"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main() 
