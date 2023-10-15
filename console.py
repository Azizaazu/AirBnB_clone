#!/usr/bin/python3
"""
    Implementing the console for the HBnB project.
"""

import cmd
import shlex
import re
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State

class HBNBCommand(cmd.Cmd):
    """ Contains the entry point of the command interpreter.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "Review",
        "Amenity",
        "User",
        "Place",
        "City",
        "State"
    }

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter (Ctrl+D)"""
        print("")
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all instances."""
        args = arg.split()
        if not arg:
            print([str(val) for val in storage.all().values()])
        else:
            try:
                class_name = args[0]
                if class_name not in BaseModel.__subclasses__():
                    print("** class doesn't exist **")
                else:
                    instances = [str(val) for key, val in storage.all().items()
                                 if key.split(".")[0] == class_name]
                    print(instances)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name not in BaseModel.__subclasses__():
                    print("** class doesn't exist **")
                elif len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        if len(args) < 3:
                            print("** attribute name missing **")
                        elif len(args) < 4:
                            print("** value missing **")
                        else:
                            attribute_name = args[2]
                            attribute_value = args[3]
                            instance = storage.all()[key]
                            setattr(instance, attribute_name, attribute_value)
                            instance.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")
    def do_create(self, arg):
        """Create a new instance of a class, save it, and print the ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on class name and ID."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")
        if __name__ == "__main__":
            HBNBCommand().cmdloop()
