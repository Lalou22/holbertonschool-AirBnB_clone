#!/usr/bin/python3
"""
Entry point for the command interpreter of the HBNB application
"""
import cmd
import models
from datetime import datetime
from models import allclasses
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class for the Holberton Clone AirBnB proyect.
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """
        Typing "EOF" Exits the program
        """
        quit()

    def do_quit(self, arg):
        """
        Typing "quit" Exits the program
        """
        quit()

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in allclasses:
            instance = eval(args[0])()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in allclasses:
            if len(args) > 1:
                key = args[0] + "." + args[1]
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
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in allclasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dict_objs = models.storage.all()
            for key in dict_objs.keys():
                obj_id = dict_objs[key].id
                obj_name = dict_objs[key].__class__.__name__
                if (args[1] == obj_id and args[0] == obj_name):
                    del dict_objs[key]
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        args = arg.split()
        if len(args) == 0:
            print([str(v) for k, v in storage.all().items()])
        else:
            if args[0] not in allclasses:
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in storage.all().items()
                       if type(v).__name__ == args[0]])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in allclasses:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            for key, val in storage.all().items():
                trgt_name = val.__class__.__name__
                trgt_id = val.id
                if trgt_name == args[0] and trgt_id == args[1]:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def default(self, arg):
        """
        Function created to deal with the advanced task
        Where you must read and execute instructions
        based on the classes
        """
        args = arg.split('.', 1)
        if len(args) == 2:
            if args[0] in allclasses:
                funct = args[1].split('(', 1)
                dic_fun = ["all", "count", "show", "destroy", "update"]

                if funct[0] in dic_fun:
                    if funct[0] == "all":
                        self.do_all(str(args[0]))

                    if funct[0] == "count":
                        count = 0
                        for k, v in storage.all().items():
                            if type(v).__name__ == args[0]:
                                count = count + 1
                        print(count)

                    if funct[0] == "show":
                        inner_str = funct[1].split('"')[1::2]
                        inner_str = args[0] + " " + str(inner_str[0])
                        self.do_show(inner_str)

                    if funct[0] == "destroy":
                        inner_str = funct[1].split('"')[1::2]
                        inner_str = args[0] + " " + str(inner_str[0])
                        self.do_destroy(inner_str)

                    if funct[0] == "update":
                        temp_dict = funct[1].split("{")
                        if len(temp_dict) == 2:
                            if temp_dict[1][-1] == ')':
                                temp_dict[1] = temp_dict[1][:-1]
                            str_dic = "{" + temp_dict[1]
                            up_dict = eval(str_dic)
                            funct[1] = temp_dict[0]
                        else:
                            up_dict = {}

                        up_args = funct[1].split(",")
                        if len(up_args) == 2 or len(up_args) == 3:
                            up_id = up_args[0].split('"')[1::2][0]

                            if len(up_args) == 3:
                                up_key = up_args[1].split('"')[1::2][0]
                                up_val = up_args[2].split('"')[1::2][0]
                                up_dict[up_key] = up_val

                            for key_, val_ in up_dict.items():
                                inner_str = {}
                                inner_str = args[0] + " " + str(up_id) + " "
                                inner_str = inner_str + str(key_) + " "
                                inner_str = inner_str + '"' + str(val_) + '"'
                                self.do_update(inner_str)
                else:
                    print("** invalid command **")
        else:
            print("** invalid command **")

    def emptyline(line):
        """
        Empty lines will go to the next input loop.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
