#!/usr/bin/python3
""" File define BaseModel file """
import json
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If kwargs is not empty:
            Each key of the kwargs dictionary is\
                an attribute name (except for '__class__').
            Each value of the kwargs dictionary is\
                the value of the corresponding attribute.

        If kwargs is empty:
            Creates a new instance with a\
                new id and current datetime for created_at.

        Note: The 'created_at' and 'updated_at'\
            attributes in kwargs should be in string format,
        but they will be converted to\
            datetime objects inside the BaseModel instance.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        This method should be called whenever changes are made to the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing all the attributes of the instance.
                  The 'class' key is added with the name of the object's class.
                  The 'created_at' and 'updated_at' attributes converted to ISO
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the instance.
        The string format :"[<class name>] (<id>) <dictionary representation>"
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)
