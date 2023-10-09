#!/usr/bin/python3
"""
Defines a function to add a new attribute to an object if it's possible.
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
