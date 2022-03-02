#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json

class HBNBCommand(cmd.Cmd):

    list_verif = ["BaseModel"]
    prompt = "(hbnb) "

    def emptyarg(self):
        """
            empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_quit(self, arg):
        """
            quit to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
            EOF to exit the program
        """
        return True

    def do_create(self, arg):
        """
            create new istance of basemodel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            instance = eval(arg)()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            string representation of an instance
            based on the class name and id
        """
        list_arg = arg.split(" ")
        i = 0
        key = list_arg[0] + '.' + list_arg[1]

        print(list_arg)
        if not list_arg[i]:
            print("** class name missing **")
            return

        if list_arg[i] not in HBNBCommand.list_verif:
            print("** class doesn't exist **")
            return

        if (len(list_arg) < 2):
            print("** instance id missing **")
        elif not key in FileStorage.all(self):
            print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
        """

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """


    def do_update(self, arg):    
        """
            Updates an instance based on the class name and id
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
