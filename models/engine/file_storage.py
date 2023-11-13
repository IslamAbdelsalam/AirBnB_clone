#!/usr/bin/python3
import json
import datetime
"""
FileStorage class model
"""


class DateTimeEncoder(json.JSONEncoder):
    """
    This class is used to convert a datetime object into string format.
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return super().default(obj)


class FileStorage():
    """
    This class represents the file storage in
    which all files are stored and retrieved from.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the list of file objects in the database.
        """
        return self.__objects

    @classmethod
    def new(self, obj):
        """
        Adds an object to the database.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Saves the current state of the database to disk.
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value if isinstance(value, dict) else value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file, cls=DateTimeEncoder)

    def reload(self):
        """
        Reloads objects from a saved state
        """
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    FileStorage.__objects = json.load(file)
            except FileNotFoundError:
                return

            for key, value in FileStorage.__objects.items():
                FileStorage.new(value)
