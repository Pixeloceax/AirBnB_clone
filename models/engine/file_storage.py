#!/usr/bin/python3
""" storage Module """

import json
from datetime import datetime
from shutil import ExecError 
from models import *

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
        with open(self.__file_path, "a+") as file:
            json.dump(self.objects, file)

    def reload(self):
        """
            raise json file
        """
        try:
            f = open(self.file_path, "r")
            self.__objects = json.load(f)

        except Exception as f:
            pass