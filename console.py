# Command interpreter in Python

import cmd
import models
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and         prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        all_classes = storage.all()
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        new_instance = all_classes[class_name]()
        new_instance.save()
        print(new_instance.id)
    def do_show(self, line):
        """Shows an instance of a model"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
            return

        cls_name = tokens[0]
        if not hasattr(models, cls_name):
            print(f"** class doesn't exist **")
            return

        if len(tokens) == 1:
            print("** instance id missing **")
            return

        id = tokens[1]
        instances = cls_name.all()
        instance = instances.get(id)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)


    def do_destroy(self, line):
        """Destroys an instance of a model"""
        tokens = line.split()
        if len(tokens) == 0:
            print("** class name missing **")
        return

        cls_name = tokens[0]
        if not hasattr(models, cls_name):
            print(f"** class doesn't exist **")
        return

        if len(tokens) == 1:
            print("** instance id missing **")
        return

        id = tokens[1]
        instances = cls_name.all()
        instance = instances.get(id)
        if instance is None:
            print("** no instance found **")
        else:
            instances.delete(instance)
            instances.save()
            print(f"** {instance.__class__.__name__} {instance.id} deleted **")
    
    def do_all(self, line):
        """Prints all instances of a model"""
        tokens = line.split()
        cls_name = tokens[0] if tokens else None

        if cls_name and not hasattr(models, cls_name):
            print(f"** class doesn't exist **")
        return

        if cls_name:
            instances = getattr(models, cls_name).all()
        else:
            instances = []
        for cls in models.__dict__.values():
            if isinstance(cls, type) and issubclass(cls, BaseModel):
                class_instances = cls.all()
                instances.extend(class_instances)

        if not instances:
            print("** No instances found **")
        else:
            print("[")
            for instance in instances:
                print(f"  {instance}", end=",")
            print("]")

    
    def do_update(self, line):
        """Updates an instance of a model"""
        tokens = line.split()
        if len(tokens) < 4:
            if len(tokens) == 0:
                print("** class name missing **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return

        cls_name = tokens[0]
        if not hasattr(models, cls_name):
            print(f"** class doesn't exist **")
            return

        id = tokens[1]
        instances = cls_name.all()
        instance = instances.get(id)
        if instance is None:
            print("** no instance found **")
            return

        attr_name = tokens[2]
        if attr_name in ["id", "created_at", "updated_at"]:
            print(f"** {attr_name} cannot be updated **")
            return

        attr_value = " ".join(tokens[3:])
        if attr_value == "":
            print("** value missing **")
            return


        attr_type = type(getattr(instance, attr_name))
        if attr_type == str:
            new_value = attr_value
        elif attr_type == int:
            new_value = int(attr_value)
        elif attr_type == float:
            new_value = float(attr_value)
        else:
            print("** Only simple attributes (str, int, float) can be updated **")
            return

        setattr(instance, attr_name, new_value)
        instances.save()
        print(f"** {instance.__class__.__name__} {instance.id} updated **")


    def do_quit(self, arg):
        """This quits or exits the program"""
        return True

    # Aliasing
    do_EOF = do_quit

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
