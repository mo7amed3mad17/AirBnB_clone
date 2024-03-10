#!/usr/bin/python3
""" File with FileStorage class """
from models.base_model import BaseModel
import json


class FileStorage:
    """ FileStorage class as storage engine

    Attributes:
        __file_path (str): name of the file to save objects
        __objects (dict): A dict of objects that have instantiated
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
       """ Returns the dictionary __objects """
       return FileStorage.__objects


    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): The object to set in __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """  serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = eval(class_name)
                    obj = class_obj(**value)

            FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
