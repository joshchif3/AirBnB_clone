#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
import json
import os


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
        """REMEMBER TO WRITE IT AGAIN"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                self.__objects = {
                    k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_dict.items()
                }
