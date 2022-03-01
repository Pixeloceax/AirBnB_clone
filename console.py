#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

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

        """




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
