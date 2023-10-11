#!/usr/bin/python3
"""
Module: base_model.py
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Creates a new BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            args (any): Not used
            kwargs (dict): Key/Value pairs to use as attributes
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Updates the most recent change time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Returns the string representation of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
