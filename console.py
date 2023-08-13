#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class definition HBNBCommand which inherits from cmd.Cmd"""
    prompt = "(hbnb)"

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
        if arg is None:
            print("** class name missing **")
        elif hasattr(sys.modules[__name__], arg):
            cls = getattr(sys.modules[__name__], arg)
            instance = cls()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = class_name + "." + instance_id
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
