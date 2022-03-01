#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd

from click import prompt
from models import storage
import json
from models import base_model

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """quit to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
