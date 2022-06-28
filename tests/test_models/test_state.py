#!/usr/bin/python3
"""
Unittest base_model
Test cases for class State
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for State class
    """

    def test_is_subclass(self):
        """
        Test if the State class is a subclass of BaseModel
        """
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)
        self.assertTrue(hasattr(new_state, "id"))
        self.assertTrue(hasattr(new_state, "created_at"))
        self.assertTrue(hasattr(new_state, "updated_at"))

    def test_name_attr(self):
        """
        Test State attribute name (Empty string)
        """
        new_state = State()
        self.assertTrue(hasattr(new_state, "name"))
        self.assertEqual(new_state.name, "")

    def test_str(self):
        """
        Test the __str__ method
        """
        new_state = State()
        string = "[State] ({}) {}".format(new_state.id, new_state.__dict__)
        self.assertEqual(string, str(new_state))
