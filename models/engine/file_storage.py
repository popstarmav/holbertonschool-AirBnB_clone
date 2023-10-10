#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        object_dict = {}
        for obj_key, obj_value in FileStorage.__objects.items():
            object_dict[obj_key] = obj_value.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(object_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                object_dict = json.load(file)
                for obj_key, obj_value in object_dict.items():
                    class_name = obj_value["__class__"]
                    del obj_value["__class__"]
                    obj_instance = eval(class_name)(**obj_value)
                    FileStorage.__objects[obj_key] = obj_instance
        except FileNotFoundError:
            return
