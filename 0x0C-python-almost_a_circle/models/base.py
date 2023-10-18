#!/usr/bin/python3
"""Defines a base class"""

import json
import os


class Base:
    """The `base` of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the new instace of the class (the constructor)"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of `list_dictionaries`"""
        if list_dictionaries and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        f_name = cls.__name__ + '.json'
        with open(f_name, 'w') as f:
            if list_objs:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dictionaries))
            else:
                f.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string`"""
        if json_string and json_string != "[]":
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances in the json file called
        `<Class name>.json`
        """
        f_name = cls.__name__ + ".json"
        list_instances = []
        if os.path.exists(f_name):
            with open(f_name, 'r') as f:
                list_dictionaries = Base.from_json_string(f.read())
                for d in list_dictionaries:
                    list_instances.append(cls.create(**d))
        return list_instances
