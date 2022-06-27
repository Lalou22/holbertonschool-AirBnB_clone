#!/usr/bin/python3
"""
Class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        super() function is used to give access to methods and properties
        of a parent, in this case to the __init__ funciton
        """
        super().__init__(*args, **kwargs)
