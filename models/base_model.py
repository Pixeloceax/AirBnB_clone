#!/usr/bin/python3
""" Base Module """

import uuid
from datetime import datetime
import models


class BaseModel:
    """
        class for object hierarchy
    """
    def __init__(self, *args, **kwargs):
        """
            comment
        """
        if args is not None:
            pass
        if len(args) > 0:
            pass

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            return string represantation of an istance
        """
        return("[{}] ({}) {}").format(type(self).__name__,
                                      self.id, self.__dict__)

    def to_dict(self):
        """
            return a dictionary represantation of an istance
        """
        my_dictionary = self.__dict__.copy()
        my_dictionary["__class__"] = type(self).__name__
        my_dictionary["created_at"] = my_dictionary["created_at"].isoformat()
        my_dictionary["updated_at"] = my_dictionary["updated_at"].isoformat()
        return my_dictionary

    def save(self):
        """
            update the upadated_at in the current date time
        """
        self.updated_at = datetime.now()
        models.storage.save()
