#!/usr/bin/python3
import uuid
import datetime
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Constructor for the base model."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ["created_at", "updated_at"]:
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            if storage:
                storage.new(self)

    def __str__(self):
        """Returns a string representation of this object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves an instance to the database."""
        self.updated_at = datetime.datetime.now()
        if storage:
            storage.save()

    def to_dict(self):
        """Converts this object into a dictionary that can be serialized as JSON."""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["created_at"] = data.get("created_at").isoformat()
        data["updated_at"] = data.get("updated_at").isoformat()
        return data
