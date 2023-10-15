#!/usr/bin/python3
"""
    Defines the FileStorage class Module 
"""
import json
import models

class FileStorage:
    """
        Serializes the instances of a JSON file and deserializes of a JSON file.
    """
    __file_path = "file.json"
    __objects = {}


    def new(self, obj):
        """
        Sets the new obj into __objects
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def all(self):
        """
        Returns the new dictionary on filestorage
        """
        return self.__objects
    
    def save(self):
        """
        Serializes the new objects into the JSON file
        """
        object_dict = {}
        for key, val in FileStorage.__objects.items():
            object_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(object_dict, fd)

    def reload(self):
        """
        Reups file and deserializes the JSON into __objects class
        """

        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

