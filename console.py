#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

import shlex


class HBNBCommand(cmd.Cmd):
    """Class definition HBNBCommand which inherits from cmd.Cmd"""
    prompt = "(hbnb)"
    classes_map = ["BaseModel", "User", "Amenity",
                   "City", "Place", "Review", "State"]

    def do_quit(self, arg):
        """Exit the program with the Quit command"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def emptyline(self):
        """To do nothing when an empty line is the entry."""
        pass

    def do_create(self, arg):
        """Create method that creats an object"""
        if arg:
            if hasattr(sys.modules[__name__], arg):
                cls = getattr(sys.modules[__name__], arg)
                instance = cls()
                models.storage.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy method that destroys an object."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = models.storage.all()
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """To print all objects or objects of a specific class"""
        objects = models.storage.all()
        if not arg.split():
            for val in objects.values():
                print(f"{str(val)}", end="")
            print()
        else:
            if arg not in self.classes_map:
                print("** class doesn't exist **")
            else:
                for val in objects.values():
                    if type(val).__name__ == arg:
                        print(f"{str(val)}", end="")
                print()

    def do_update(self, arg):
        """Update method to update an attribute in a given object"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in self.classes_map:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            objects = models.storage.all()
            instance_key = f"{class_name}.{instance_id}"
            if instance_key not in objects:
                print("** no instance found **")
                return
            instance = objects[instance_key]
            if hasattr(instance, args[2]):
                attribute_type = type(getattr(instance, args[2]))
                try:
                    attribute_value = attribute_type(args[3])
                    setattr(instance, args[2], attribute_value)
                    models.storage.save()
                except ValueError:
                    print("** Invalid value for attribute type **")
            else:
                print("** Attribute doesn't exist in the instance **")
        except NameError:
            print("** class doesn't exist **")
