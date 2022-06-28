#!/usr/bin/python3
"""
Unittest console
Test cases for class HBNBCommand
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import pycodestyle
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Test cases for the class HBNBCommand
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup for the test
        """
        cls.new_console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """
        At the end of the test this will delete the console
        """
        del cls.new_console

    def tearDown(self):
        """
        Remove the json file created as a result
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
        p = style.check_files(['console.py'])
        self.assertEqual(p.total_errors, 0, "fix pycodestyle")

    def test_docstrings(self):
        """
        Checking docstrings
        """
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)

    def test_EOF(self):
        """
        Test quit command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.new_console.onecmd("EOF")
            self.assertEqual('', f.getvalue())
            
    def test_quit(self):
        """
        Test quit command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.new_console.onecmd("quit")
            self.assertEqual('', f.getvalue())


    def test_create(self):
        """
        Test create command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create dummy_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create BaseModel")
            self.new_console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("all User")
            self.assertEqual(
                "[\"[User]", f.getvalue()[:8])

    def test_show(self):
        """
        Test show command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("show dummy_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("show BaseModel dummy_instance")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """
        Test destroy command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("destroy dummy_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("destroy BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("destroy BaseModel dummy_instance")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """
        Test all command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("all dummy_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("all Review")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """
        Test update command input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update dummy_class")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update BaseModel dummy_instance")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("update User " + my_id + "Name")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_class_all(self):
        """
        Test for the ModelBase.all()
        """
        abs_path  = os.path.dirname(os.path.abspath("console.py"))
        json_path = os.path.join(abs_path, "file.json")
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create BaseModel")
            obj = f.getvalue()
            my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("BaseModel.all()")
            with open(json_path) as jsonFile:
                jsonObject = json.load(jsonFile)
                test_text = "BaseModel." + str(my_id)
                self.assertEqual(jsonObject[test_text]["id"], str(my_id))

    def test_class_count(self):
        """
        Test for the Review.count()
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("create Review")
            obj = f.getvalue()
            my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("Review.count()")
            self.assertEqual("1\n", f.getvalue())
        
    def test_empty(self):
        """
        Test empty line input
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.new_console.onecmd("\n")
            self.assertEqual('', f.getvalue())
