#!/usr/bin/python3
"""
    Main Console program
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

import models
from models import storage
from models.base_model import BaseModel
from shlex import split


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """ defines console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on Ctrl+D (EOF)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to JSON file"""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = BaseModel()
            obj.save()
            print(obj.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = split(arg)

        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            try:
                cls = models.classes[args[0]]
                instances = cls.all()
                print([str(obj) for obj in instances])
            except Exception:
                print("** class doesn't exist **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = split(arg)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        try:
            cls = models.classes[args[0]]
            count = cls.count()
            print(count)
        except Exception:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id with a dictionary"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return

        key = args[0] + '.' + args[1]
        objects = storage.all()

        if key in objects:
            obj = objects[key]
            try:
                obj_dict = eval(args[2])
                if isinstance(obj_dict, dict):
                    for attr, value in obj_dict.items():
                        setattr(obj, attr, value)
                    obj.save()
                else:
                    print("** invalid dictionary **")
            except Exception:
                print("** invalid dictionary **")
        else:
            print("** no instance found **")

    def do_class_show(self, arg):
        """Show an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_class_destroy(self, arg):
        """Destroy an instance based on the class name and id"""
        args = split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
