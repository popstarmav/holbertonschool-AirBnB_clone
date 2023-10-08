#!/usr/bin/python3
import uuid
from datetime import datetime
import json


class BaseModel:
    """BaseModel class with common attributes and methods."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                    ))
                elif key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """Update the updated_at attribute to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, json.dumps(self.__dict__))

    def __repr__(self):
        """Return a string representation of the BaseModel instance."""
        return str(self.to_dict())

    def from_dict(self, dict):
        """Update instance attributes from a dictionary."""
        for key, value in dict.items():
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f"
                ))
            else:
                setattr(self, key, value)
