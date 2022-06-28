#!/usr/bin/python3
"""
Entry point for the command interpreter of the HBNB application
"""
import cmd
import models
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
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_EOF(self, arg):
        """
        Typing "EOF" Exits the program
        """
        return True

    def do_quit(self, arg):
        """
        Typing "quit" Exits the program
        """
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
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
        if args[0] in self.classes:
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
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            dict_objs = models.storage.all()
            for key in dict_objs.keys():
                if args[1] == dict_objs[key].id:
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
            if args[0] not in self.classes:
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
        if args[0] not in self.classes:
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

    def emptyline(line):
        """
        Empty lines will go to the next input loop.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()