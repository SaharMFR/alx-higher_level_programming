#!/usr/bin/python3
"""Defines a base class"""

import json


class Base:
    """The `base` of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
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
        f_name = = cls.__name__ + '.json'
        with open(f_name, 'w') as f:
            if list_objs:
                list_dictionaries = obj.to_dictionary() for obj in list_objs
                f.write(Base.to_json_string(list_dictionaries))
            else:
                f.write("[]")
