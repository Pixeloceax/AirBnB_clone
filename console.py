#!/usr/bin/python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
import shlex
from models import storage
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes_verif = {"BaseModel": BaseModel, "User": User,
                 "State": State, "City": City,
                 "Amenity": Amenity, "Place": Place, "Review": Review}


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

                if key in storage.all():
                    print(storage.all()[key])

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

                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()

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
            for value in storage.all().values():
                obj_list.append(str(value))
            print("]")
            print(", ".join(obj_list), end="")
            print("[")

        elif spliting[0] in classes_verif:
            for key in storage.all():
                if spliting[0] in key:
                    obj_list.append(str(storage.all()[key]))
            print("[")
            print(", ".join(obj_list), end="")
            print("]")

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
            comment
        """
        args = arg.split()
        kw = ".".join(args[:2])
        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif ".".join(args[:2]) not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            kw = ".".join(args[:2])
            atributs = args[2]
            value = args[3]
            _dict = models.storage.all()[kw].__dict__
            _dict[atributs] = value
            models.storage.save()

    def default(self, arg):
        """
            retrieve all instances of a class by using multiple options
        """
        spliting = arg.split('.')
        test = spliting[1]
        test = test.split("\"")
        all = "all()"
        count = "count()"
        show = "show("
        destroy = "destroy("
        try:
            if spliting[1] == all:
                self.do_all(spliting[0])
        except Exception:
            pass
        try:
            if spliting[1] == count:
                self.do_count(spliting[0])
        except Exception:
            pass
        try:
            if test[0] == show:
                arguments = spliting[0] + " " + test[1]
                self.do_show(arguments)
        except Exception:
            pass
        try:
            if test[0] == destroy:
                arguments = spliting[0] + " " + test[1]
                self.do_destroy(arguments)
        except Exception:
            pass

    def do_count(self, arg):
        """
            retrieve the number of instances of a class
        """
        counter = 0
        for key in storage.all().keys():
            if arg in key:
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
