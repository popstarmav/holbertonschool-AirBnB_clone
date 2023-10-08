#!/usr/bin/python3
import cmd
import sys
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """Console command interpreter class."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, line):
        """Exit the console."""
        sys.exit(0)

    def do_EOF(self, line):
        """Exit the console with Ctrl+D."""
        print()  # Print a newline
        sys.exit(0)

    def do_create(self, line):
        """Create a new instance of a class."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show the string representation of an instance."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + "." + args[1]
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on its ID."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + "." + args[1]
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Show all instances of a class."""
        args = shlex.split(line)
        instances = []
        if len(args) == 0:
            for obj in models.storage.all().values():
                instances.append(str(obj))
            print("[{}]".format(", ".join(instances)))
            return
        try:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    instances.append(str(obj))
            print("[{}]".format(", ".join(instances)))
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update an instance attribute."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            key = args[0] + "." + args[1]
            obj_dict = models.storage.all()
            if key not in obj_dict:
                print("** no instance found **")
                return
            obj = obj_dict[key]
            setattr(obj, args[2], args[3])
            obj.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_count(self, line):
        """Count the number of instances of a class."""
        args = shlex.split(line)
        count = 0
        if len(args) == 0:
            for obj in models.storage.all().values():
                count += 1
            print(count)
            return
        try:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    count += 1
            print(count)
        except KeyError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
