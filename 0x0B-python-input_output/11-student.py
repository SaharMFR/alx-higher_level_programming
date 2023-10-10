#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
