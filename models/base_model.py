#!/usr/bin/python3
"""Defines a new class BaseModel."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Creates a new BaseModel instance."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel.

        Args:
            args: Unused
            kwargs (dict): Key/Value pairs to use as attributes
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(self, key, value)

                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, date_format))

        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime and saves to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the object for JSON serialization."""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name()
        return obj_dict

    def __str__(self):
        """Returns a string representation of the object."""
        cls_name = self.__class__.__name
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
