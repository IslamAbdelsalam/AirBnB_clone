#!/usr/bin/python3
import cmd
"""
"""
class HBNBCommand(cmd.Cmd):
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
