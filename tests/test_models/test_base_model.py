#!/usr/bin/python3
"""
Unittest base_model
Test cases for class BaseModel
"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from uuid import uuid4
import time
import os
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """
    Test case for class BaseModel
    """
    my_model = BaseModel()

    def setUp(self):
        """
        Set up test methods
        """
        pass

    def teardown(self):
        """
        Tears down test methods
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Test for pycodestyle
        Example https://campus.datacamp.com/courses/
        software-engineering-for-data-scientists-in-python/
        software-engineering-data-science?ex=8
        """
        style = pycodestyle.StyleGuide()
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_check_functions(self):
        """
        Test to check if the class contains the wanted funcionts
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attr(self):
        """
        Test to check if the class contains the wanted attributes
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """
        Test to check for an empty initialization of the
        BaseModel object
        """
        self.assertTrue(isinstance(self.my_model, BaseModel))

    def test_save(self):
        """
        Test for the save function in the Base_Model class
        """
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict(self):
        """
        Test for the to_dict function in the Base_Model class
        """
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)

    def test_BaseModel(self):
        """
        Creates and test a model using the my_model class variable
        """
        self.my_model.name = "Lalo"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()
        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def test_empty_instance(self):
        """
        Creates and test a model using an empty base model
        """
        new_model = BaseModel()
        self.assertEqual(str(type(new_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(new_model, BaseModel)
        self.assertTrue(issubclass(type(new_model), BaseModel))

    def test_datetime_created_at(self):
        """
        Test if created_at is a datetime obj
        """
        self.assertTrue(type(self.my_model.created_at) is datetime)

    def test_datetime_updated_at(self):
        """
        Test if updated_at is a datetime obj
        """
        self.assertTrue(type(self.my_model.updated_at) is datetime)

    def test_to_str(self):
        test_id = self.my_model.id
        test_dic = self.my_model.__dict__
        str_to_cmp = "[BaseModel] ({}) {}".format(test_id, test_dic)
        self.assertEqual(str(self.my_model), str_to_cmp)


if __name__ == '__main__':
    unittest.main()
