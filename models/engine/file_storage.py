#!/usr/bin/python3
""" storage Module """

import json
from datetime import datetime 
from models.base_model import BaseModel

class FileStorage:
    """
        class for object storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self): 
        """
            return the dictionary object
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
            set new obj
        """
        key = "{}.{}".format(type(self).__name__, self.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """
            save to the json file
        """

