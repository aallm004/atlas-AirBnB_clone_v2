#!/usr/bin/python3
"""test_state"""
import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Test the class State"""

    def test_init(self):
        """Unit tests """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
