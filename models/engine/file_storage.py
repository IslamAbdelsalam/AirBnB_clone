import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    @classmethod
    def new(cls, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        cls.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(self.__objects, file, default=lambda o: o.__dict__)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            return
