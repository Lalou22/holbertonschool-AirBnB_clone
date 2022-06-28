#!/usr/bin/python3
"""
Class FileStorage that serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes instances to a JSON file and deserializes JSON
    file to instances.
    Private Class attributes
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects
    Public instance methods
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key
    save(self): serializes __objects to the JSON file
    reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {"Amenity": Amenity, "BaseModel": BaseModel,
                 "City": City, "Place": Place, "Review": Review,
                 "State": State, "User": User}

    def all(self):
        """
        Public method that returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        dic = {}
        for id, object in self.__objects.items():
            dic[id] = object.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as myfile:
            json.dump(dic, myfile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode="r", encoding="UTF-8") as myfile:
                ob = json.load(myfile)
            for id, dic in ob.items():
                value = models.BaseModel(**dic)
                self.__objects[id] = value
        except FileNotFoundError:
            pass
