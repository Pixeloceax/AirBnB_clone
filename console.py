#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
import shlex

classes_verif = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
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
            Prints the string representation of an instance based on the class name and id
        """
        spliting = shlex.split(arg)

        if len(spliting) == 0:
            print("** class name missing **")

        if spliting[0] in classes_verif:

            if len(spliting) > 1:
                key = spliting[0] + '.' + spliting[1]

                if key in models.storage.all():
                    print(models.storage.all()[key])

                else:
                    print("** no instance found **")

            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """

        """
        
    def do_all(self, arg):
        """
        
        """


    def do_update(self, arg):    
        """
        
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
