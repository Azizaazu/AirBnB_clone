#!/usr/bin/python3
"""Defines the BaseModel class."""

import models
from uuid import uuid4 
from datetime import datetime

class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """ Initialization of new basmodel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
         """Update the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
