#!/usr/bin/python3
"""Defines a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes the Object `my_obj` to the text file `filename`
    using a JSON representatoin.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
