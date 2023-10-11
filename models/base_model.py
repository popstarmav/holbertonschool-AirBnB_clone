#!/usr/bin/python3
from datetime import datetime
import json
import models
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = class_name
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
