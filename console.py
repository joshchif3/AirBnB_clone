#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
