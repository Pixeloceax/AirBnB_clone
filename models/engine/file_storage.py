#!/usr/bin/python3
""" storage Module """

import json
from models.user import User
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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
            save to the json file
        """
        with open(self.__file_path, 'w+') as fp:
            ln = json.dumps(FileStorage.__objects)
            fp.writelines(ln)
        fp.close

    def reload(self):
        """
            raise json file
        """
        try:
            with open(self.__file_path) as fp:
                fn = fp.read()
                FileStorage.__objects = json.loads(fn)
        except Exception:
            pass
