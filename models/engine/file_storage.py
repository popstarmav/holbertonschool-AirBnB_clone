#!/usr/bin/python3
import json


class FileStorage:
    """FileStorage class for storing and retrieving objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieve all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save objects to JSON file."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Load objects from JSON file."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
