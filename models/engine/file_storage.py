#!/usr/bin/python3
""" module containing FileStorage used for file storage"""

from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.base_model import BaseModel
from models.place import Place
from models.state import State
import json

class FileStorage:
    """ Represent storage instances to and from JSON file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
       """Return dicr __obj."""
        return self.__objects

    def new(self, obj):
        """ creates a new object and saves it to __objects"""
        key = "{}.{}".format(obj.__class__.____name, obj.id)
        self.__objects[key] = obj

    def save(self):
         """update the JSON file to reflect any change in the objects"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
         """ update __objects dict"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_class = models[class_name]
                    self.__objects[key] = obj_class(**obj_data)
        except FileNotFoundError:
            pass
