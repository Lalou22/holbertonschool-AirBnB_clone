#!/usr/bin/python3
"""
Unittest base_model
Test cases for class User
"""

import unittest
import time
import pycodestyle
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for User class
    """

    def test_is_subclass(self):
        """
        Test if the User class is a subclass of BaseModel
        """
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)
        self.assertTrue(hasattr(new_user, "id"))
        self.assertTrue(hasattr(new_user, "created_at"))
        self.assertTrue(hasattr(new_user, "updated_at"))

    def test_email_attr(self):
        """
        Test User attribute email (Empty string)
        """
        new_user = User()
        self.assertTrue(hasattr(new_user, "email"))
        self.assertEqual(new_user.email, "")

    def test_password_attr(self):
        """
        Test User attribute password (Empty string)
        """
        new_user = User()
        self.assertTrue(hasattr(new_user, "password"))
        self.assertEqual(new_user.password, "")

    def test_first_name_attr(self):
        """
        Test User has attribute first_name (Empty string)
        """
        new_user = User()
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertEqual(new_user.first_name, "")

    def test_last_name_attr(self):
        """
        Test User has attribute last_name (Empty string)
        """
        new_user = User()
        self.assertTrue(hasattr(new_user, "last_name"))
        self.assertEqual(new_user.last_name, "")

    def test_str(self):
        """
        Test the __str__ method
        """
        new_user = User()
        string = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertEqual(string, str(new_user))
