#!/usr/bin/python3
"""
class BaseModel that defines all common attributes or methods
for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Public instance attributes
    id: uuid when an instance is created
    created_at: Datetime when an instance is created
    updated_at: Current datetime when an instance is
    created and it will be updated every time
    Public instance methods
    save(self): updates the public instance attributes
    to_dict(self): returns a dictionary of the instance
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiation of class (id, created_at, updated_at)
        *args won’t be used
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method returns the string representation
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        """
        dic = vars(self).copy()
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        return dic
