#!/usr/bin/python3
"""
Class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes
    name: string - empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        super() function is used to give access to methods and properties
        of a parent, in this case to the __init__ funciton
        """
        super().__init__(*args, **kwargs)
