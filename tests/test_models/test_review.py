#!/usr/bin/python3
"""
Unittest base_model
Test cases for class Review
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """

    def test_is_subclass(self):
        """
        Test if the Review class is a subclass of BaseModel
        """
        new_rev = Review()
        self.assertIsInstance(new_rev, BaseModel)
        self.assertTrue(hasattr(new_rev, "id"))
        self.assertTrue(hasattr(new_rev, "created_at"))
        self.assertTrue(hasattr(new_rev, "updated_at"))

    def test_place_id_attr(self):
        """
        Test Review attribute place_id (Empty string)
        """
        new_rev = Review()
        self.assertTrue(hasattr(new_rev, "place_id"))
        self.assertEqual(new_rev.place_id, "")

    def test_user_id_attr(self):
        """
        Test Review attribute password (Empty string)
        """
        new_rev = Review()
        self.assertTrue(hasattr(new_rev, "user_id"))
        self.assertEqual(new_rev.user_id, "")

    def test_text_attr(self):
        """
        Test Review has attribute first_name (Empty string)
        """
        new_rev = Review()
        self.assertTrue(hasattr(new_rev, "text"))
        self.assertEqual(new_rev.text, "")

    def test_str(self):
        """
        Test the __str__ method
        """
        new_rev = Review()
        string = "[Review] ({}) {}".format(new_rev.id, new_rev.__dict__)
        self.assertEqual(string, str(new_rev))
