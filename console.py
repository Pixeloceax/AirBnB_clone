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
    """
        console
    """

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
            print("** class name missing **")
            return False

        if split_arg[0] in classes_verif:

            if len(split_arg) > 1:
                key = split_arg[0] + '.' + split_arg[1]

                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()

                else:
                    print("** no instance found **")

            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

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
            print("]", end="")
            print(", ".join(obj_list), end="")
            print("[")

        elif spliting[0] in classes_verif:
            for key in storage.all():
                if spliting[0] in key:
                    obj_list.append(str(storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
            comment
        """
        spliting = arg.split()
        if len(spliting) == 0:
            print("** class name missing **")
            return False

        if spliting[0] in classes_verif:

            if len(spliting) > 1:
                key = spliting[0] + '.' + spliting[1]

                if key in storage.all():

                    if len(spliting) > 2:

                        if len(spliting) > 3:
                            setattr(storage.all()[key],
                                    spliting[2], spliting[3])
                            storage.all()[key].save()

                        else:
                            print("** value missing **")

                    else:
                        print("** attribute name missing **")

                else:
                    print("** no instance found **")

            else:
                print("** instance id missing **")

        else:
            print("** class doesn't exist **")

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
                args = spliting[0] + " " + test[1]
                self.do_show(args)
        except Exception:
            pass
        try:
            if test[0] == destroy:
                args = spliting[0] + " " + test[1]
                self.do_destroy(args)
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
