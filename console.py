#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
import shlex
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes_verif = {"BaseModel": BaseModel, "User": User}


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
            Prints the string representation of
            an instance based on the class name and id
        """
        spliting = shlex.split(arg)

        if len(spliting) == 0:
            print("** class name missing **")
            return False

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
            Deletes an instance based on the class name and id
        """
        split_arg = shlex.split(arg)

        if len(split_arg) == 0:
            print(" class name missing ")
            return False

        if split_arg[0] in classes_verif:

            if len(split_arg) > 1:
                key = split_arg[0] + '.' + split_arg[1]

                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()

                else:
                    print(" no instance found ")

            else:
                print(" instance id missing ")

        else:
            print(" class doesn't exist ")

    def do_all(self, arg):
        """
            Prints all string representation of
            all instances based or not on the class name
        """
        spliting = shlex.split(arg)
        obj_list = []

        if len(spliting) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))

            print("".join(obj_list), end="")
            print("")

        elif spliting[0] in classes_verif:
            for key in models.storage.all():
                if spliting[0] in key:
                    obj_list.append(str(models.storage.all()[key]))

            print("".join(obj_list), end="")
            print("")

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """

        """

    def default(self, arg):
        """
            retrieve all instances of a class by using multiple options
        """
        spliting = arg.split('.')
        one = "all()"
        two = "count()"
        tgree = "show("
        four = "destroy("
        aux = spliting[1]
        aux = aux.split("\"")
        try:
            if spliting[1] == one:
                self.do_all(spliting[0])
        except Exception:
            pass
        try:
            if spliting[1] == two:
                self.do_count(spliting[0])
        except Exception:
            pass
        try:
            if aux[0] == tgree:
                arguments = spliting[0] + " " + aux[1]
                self.do_show(arguments)
        except Exception:
            pass
        try:
            if aux[0] == four:
                arguments = spliting[0] + " " + aux[1]
                self.do_destroy(arguments)
        except Exception:
            pass

    def do_count(self, arg):
        """
            retrieve the number of instances of a class
        """
        counter = 0
        for key in models.storage.all().keys():
            if arg in key:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
