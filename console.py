#!/usr/bin/python3
"""console contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import models
import shlex

options = {
    "BaseModel": BaseModel, "User": User, "Review": Review, "Amenity":
    Amenity, "State": State, "Place": Place, "City": City
    }


class HBNBCommand(cmd.Cmd):
    """class HBNB"""
    def do_EOF(self, line):
        """End of file"""
        print()
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_quit(self, line):
        """Quit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in options:
            inst = options[arg[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(inst.id)
        inst.save()

    def do_show(self, line):
        """ Prints the string representation of an instance based """
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in options:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + '.' + arg[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = shlex.split(line)
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in options:
            if len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + '.' + arg[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation of all """
        arg = shlex.split(line)
        if (len(arg) == 0 or arg[0] in options):
            list_ = []
            for key in models.storage.all():
                list_.append(str(models.storage.all()[key]))
            print(list_)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or """
        arg = line.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] in options:
            if len(arg) > 1:
                key = arg[0] + '.' + arg[1]
                if key in models.storage.all():
                    if len(arg) > 2:
                        if len(arg) > 3:
                            if arg[3][0] == '"':
                                for i in range(4, len(arg)):
                                    arg[3] += ' ' + arg[i]
                                arg[3] = arg[3].replace('"', '')
                            elif arg[3] != '"':
                                if "." in arg[3]:
                                    arg[3] = float(arg[3])
                                else:
                                    arg[3] = int(arg[3])
                            setattr(models.storage.all()[key], arg[2], arg[3])
                            models.storage.all()[key].save()
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


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
