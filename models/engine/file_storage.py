#!/usr/bin/python3
""" storage Module """

import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            save to the json file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w+') as fp:
            ln = json.dumps(new_dict)
            fp.writelines(ln)

    def reload(self):
        """
            raise json file
        """
        try:
            with open(self.__file_path, 'w+') as fp:
                dict_new = json.load(fp)
            for key, value in dict_new:
                FileStorage.__objects[key] = eval(value[__class__])(**value)
        except Exception:
            pass
