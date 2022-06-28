#!/usr/bin/python3
"""
Class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        super() function is used to give access to methods and properties
        of a parent, in this case to the __init__ funciton
        """
        super().__init__(*args, **kwargs)
