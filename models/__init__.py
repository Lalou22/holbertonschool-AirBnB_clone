#!/usr/bin/python3
from models.engine import file_storage
from models.base_model import BaseModel
from models.user import User

storage = file_storage.FileStorage()
storage.reload()
