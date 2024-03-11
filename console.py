#!/usr/bin/python3
""" File of The Console program """
import cmd
from shlex import split
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)" #our cmd
    all_classes = {"BaseModel"}

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and
        prints the id"""
        tokens = arg.split()
        class_name = tokens[0]
        if not arg:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            print(eval(class_name)().id)
            storage.save()

    def do_show(self, line):
        """Shows an instance of a model"""
        tokens = line.split()
        obj_dict = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif tokens[0] not in HBNBCommand.all_classes:
            print(f"** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(tokens[0], tokens[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(tokens[0], tokens[1])])

    def do_destroy(self, line):
        """Destroys an instance of a model"""
        tokens = line.split()
        obj_dict = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(tokens[0], tokens[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(tokens[0], tokens[1])]
            storage.save()

    def do_all(self, line):
        """Prints all instances of a model"""
        tokens = line.split()

        if len(tokens) > 0 and tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(tokens) > 0 and tokens[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(tokens) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        tokens = line.split()
        obj_dict = storage.all()

        if len(tokens) == 0:
            print("** class name missing **")
            return False
        if tokens[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return False
        if len(tokens) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(tokens[0], tokens[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(tokens) == 2:
            print("** attribute name missing **")
            return False
        if len(tokens) == 3:
            try:
                type(eval(tokens[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        instance_key = "{}.{}".format(tokens[0], tokens[1])
        instance = obj_dict[instance_key]

        if len(tokens) == 4:
            attribute_name = tokens[2]
            attribute_value = tokens[3]
            setattr(instance, attribute_name, attribute_value)
        elif isinstance(eval(tokens[2]), dict):
            attribute_dict = eval(tokens[2])
            for k, v in attribute_dict.items():
                setattr(instance, k, v)
        storage.save()

    def do_quit(self, arg):
        """This quits or exits the program"""
        return True

    do_EOF = do_quit

    def emptyline(self):
        """Called when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
