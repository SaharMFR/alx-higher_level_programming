#!/usr/bin/python3
"""
Defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Looks up for the available attributes and methods
    of `obj`
    """

    return dir(obj)