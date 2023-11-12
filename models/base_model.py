import uuid
import datetime
"""
This module contains the classes for a simple database. It is used to store data in memory and retrieve it later.
"""
class BaseModel:
    """
    This is the base model for all other models. It provides common functionality to all models.
    """
    def __init__(self):
        """Constructor for the base model."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        """Returns a string representation of this object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves an instance to the database."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Converts this object into a dictionary that can be serialized as JSON."""
        data = {}
        for key, value in vars(self).items():
            if not callable(key) and not key.startswith("_"):
                data[key] = value
        data["__class__"] = f"{type(self).__name__}"
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        return data
