#!/usr/bin/python3
"""
Unittest base_model
Test cases for class file_storage
"""

import unittest
import pycodestyle
import os
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test case for the storage engine
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test methods
        """
        cls.usr = User()
        cls.usr.first_name = "Lalo"
        cls.usr.last_name = "Rdz"
        cls.usr.email = "eduardo.roddelange@anahuac.mx"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """
        Tear down test methods
        """
        del cls.usr

    def teardown(self):
        """
        Tears down test methods
        """
        try:
            os.remove("file.json")
        except:
            pass
        
    def test_style_check(self):
        """
        Test for pycodestyle
        """
        style = pycodestyle.StyleGuide()
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_normal_cases_base_model(self):
        """
        Normal case
        """
        my_object = FileStorage()
        my_dict = my_object.all()
        self.assertIs(type(my_dict), dict)

    def test_all(self):
        """
        Test class public method all
        """
        store = FileStorage()
        dic_inst = store.all()
        self.assertIsNotNone(dic_inst)
        self.assertEqual(type(dic_inst), dict)
        self.assertIs(dic_inst, store._FileStorage__objects)

    def test_new(self):
        """
        Test class public method new
        """
        store = FileStorage()
        dic_inst = store.all()
        new_user = User()
        new_user.id = str(12345)
        new_user.name = "Eduardo"
        store.new(new_user)
        key = new_user.__class__.__name__ + "." + str(new_user.id)
        self.assertIsNotNone(dic_inst[key])

    def test_save(self):
        """
        Test that save properly saves objects to file.json
        """
        os.remove("file.json")
        storage = FileStorage()
        new_dict = {}
        classes = {"BaseModel": BaseModel, "User": User}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))
