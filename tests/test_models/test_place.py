#!/usr/bin/python3
"""
Unittest base_model
Test cases for class Place
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """

    def test_is_subclass(self):
        """
        Test if the Place class is a subclass of BaseModel
        """
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)
        self.assertTrue(hasattr(new_place, "id"))
        self.assertTrue(hasattr(new_place, "created_at"))
        self.assertTrue(hasattr(new_place, "updated_at"))

    def test_city_id_attr(self):
        """
        Test Place attribute city_id (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertEqual(new_place.city_id, "")

    def test_user_id_attr(self):
        """
        Test Place attribute user_id (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertEqual(new_place.user_id, "")

    def test_name_attr(self):
        """
        Test Place has attribute name (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "name"))
        self.assertEqual(new_place.name, "")

    def test_description_attr(self):
        """
        Test Place has attribute description (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "description"))
        self.assertEqual(new_place.description, "")

    def test_number_rooms_attr(self):
        """
        Test Place has attribute number_rooms (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertEqual(new_place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """
        Test Place has attribute number_bathrooms (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertEqual(new_place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """
        Test Place has attribute max_guest (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertEqual(new_place.max_guest, 0)

    def test_price_by_night_attr(self):
        """
        Test Place has attribute price_by_night (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertEqual(new_place.price_by_night, 0)

    def test_latitude_attr(self):
        """
        Test Place has attribute latitude (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertEqual(new_place.latitude, 0.0)

    def test_longitude_attr(self):
        """
        Test Place has attribute longitude (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertEqual(new_place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """
        Test Place attribute amenity_ids (Empty string)
        """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "amenity_ids"))
        self.assertEqual(type(new_place.amenity_ids), list)
        self.assertEqual(len(new_place.amenity_ids), 0)

    def test_str(self):
        """
        Test the __str__ method
        """
        new_place = Place()
        string = "[Place] ({}) {}".format(new_place.id, new_place.__dict__)
        self.assertEqual(string, str(new_place))
