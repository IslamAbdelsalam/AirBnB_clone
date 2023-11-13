#!/usr/bin/python3
from uuid import uuid4
import datetime
from models import storage
"""
This module contains the classes for a simple database.
It is used to store data in memory and retrieve it later.
"""


def setter(self, key, value):
    """This method sets an attribute of the object."""
    if not key.startswith("_"):
        if key == "created_at" or key == "updated_at":
            value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        setattr(self, key, value)


class BaseModel:
    """
    This is the base model for all other models.
    It provides common functionality to all models.
    """
    def __init__(self, *args, **kwargs):
        """Constructor for the base model."""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if len(kwargs.items()) != 0:
            for key, value in kwargs.items():
                setter(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of this object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves an instance to the database."""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Converts this object into dictionary that can serialized as JSON."""
        data = {}
        for key, value in vars(self).items():
            if not callable(key) and not key.startswith("_"):
                data[key] = value
        data["__class__"] = f"{type(self).__name__}"
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
