#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents a base model for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.

        Args:
            args (tuple): Unused.
            kwargs (dict): Key/Value pairs to set as attributes.
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, date_format))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name()
        return new_dict

    def __str__(self):
        """Return the string representation of the object."""
        cls_name = self.__class__.__name
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
