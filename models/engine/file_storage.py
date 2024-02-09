#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        _file_path (str): The name of the file to save objects to.
        _objects (dict): A dictionary of instantiated objects.
    """
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """Return the dictionary _objects."""
        return self._objects

    def new(self, obj):
        """Set in _objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        self._objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serialize _objects to the JSON file _file_path."""
        objects_dict = {key: value.to_dict() for key, value in self._objects.items()}
        with open(self._file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Deserialize the JSON file _file_path to _objects, if it exists."""
        try:
            with open(self._file_path, "r") as f:
                obj_dict = json.load(f)
                for obj_key, obj_value in obj_dict.items():
                    class_name = obj_value["__class__"]
                    del obj_value["__class__"]
                    obj_instance = eval(class_name)(**obj_value)
                    self._objects[obj_key] = obj_instance
        except FileNotFoundError:
            return
