#!/usr/bin/python3
"""
Unittest base_model
Test cases for class City
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for City class
    """

    def test_is_subclass(self):
        """
        Test if the City class is a subclass of BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)
        self.assertTrue(hasattr(new_city, "id"))
        self.assertTrue(hasattr(new_city, "created_at"))
        self.assertTrue(hasattr(new_city, "updated_at"))

    def test_state_id_attr(self):
        """
        Test City attribute state_id (Empty string)
        """
        new_city = City()
        self.assertTrue(hasattr(new_city, "state_id"))
        self.assertEqual(new_city.state_id, "")

    def test_name_attr(self):
        """
        Test City attribute name (Empty string)
        """
        new_city = City()
        self.assertTrue(hasattr(new_city, "name"))
        self.assertEqual(new_city.name, "")

    def test_str(self):
        """
        Test the __str__ method
        """
        new_city = City()
        string = "[City] ({}) {}".format(new_city.id, new_city.__dict__)
        self.assertEqual(string, str(new_city))
