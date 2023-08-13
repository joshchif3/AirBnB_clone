#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Class documentation -- TO BE ADDED --
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """The method all that returns the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """The method new that sets the key of the dictionary of the objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """The method save that saves the new objects as str in a file"""
        serialized = {}
        for key, val in FileStorage.__objects.items():
            serialized[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(serialized))

    def reload(self):
        """
        The method reload that reloads the dictionary from file and
        creates obj from it
        """
        try:
            with open(FileStorage.__file_path) as f:
                dictionary = json.load(f)
                for val in dictionary.values():
                    cls_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            return
