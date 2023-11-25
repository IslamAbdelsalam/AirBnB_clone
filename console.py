#!/usr/bin/python3
import cmd
"""
This is a simple command line interface for the TinyDB database.
"""


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command-line interface to interact with the TinyDB database.
    """
    def do_quit(self, arg):
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("heyy")

    def help_EOF(self):
        print("idk")

    def emptyline(self):
        pass

i = HBNBCommand()
i.prompt = "(hbnb) "
i.cmdloop()
