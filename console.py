#!/usr/bin/python3
"""
Console module for managing objects in your Airbnb clone project.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program gracefully."""
        return True

    def emptyline(self):
        """Do nothing on an empty line (pressing Enter)."""
        pass

    def do_quit(self, line):
        """Exit the program gracefully."""
        return True

    def do_create(self, arg):
        """Create a new object and print its ID."""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg.split()[0]
            if class_name not in globals() or not issubclass(globals()[class_name], BaseModel):
                print("** class doesn't exist **")
                return
            new_obj = globals()[class_name]()
            new_obj.save()
            print(new_obj.id)
        except IndexError:
            print("** class name missing **")

    def do_show(self, arg):
        """Show the string representation of an object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an object from storage."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
