#!/usr/bin/python3
"""
Unittest base_model
Test cases for class Amenity
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class
    """

    def test_is_subclass(self):
        """
        Test if the Amenity class is a subclass of BaseModel
        """
        new_amen = Amenity()
        self.assertIsInstance(new_amen, BaseModel)
        self.assertTrue(hasattr(new_amen, "id"))
        self.assertTrue(hasattr(new_amen, "created_at"))
        self.assertTrue(hasattr(new_amen, "updated_at"))

    def test_name_attr(self):
        """
        Test Amenity attribute name (Empty string)
        """
        new_amen = Amenity()
        self.assertTrue(hasattr(new_amen, "name"))
        self.assertEqual(new_amen.name, "")

    def test_str(self):
        """
        Test the __str__ method
        """
        new_amen = Amenity()
        string = "[Amenity] ({}) {}".format(new_amen.id, new_amen.__dict__)
        self.assertEqual(string, str(new_amen))
