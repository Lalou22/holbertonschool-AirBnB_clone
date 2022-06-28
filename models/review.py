#!/usr/bin/python3
"""
Class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        super() function is used to give access to methods and properties
        of a parent, in this case to the __init__ funciton
        """
        super().__init__(*args, **kwargs)
