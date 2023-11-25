import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, "w") as file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                new_dict = json.load(file)
                for key, value in new_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
