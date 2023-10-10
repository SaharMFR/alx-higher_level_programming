#!/usr/bin/python3
"""Defines a function that returns an object represented by JSON string"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by JSON string"""
    return json.loads(my_str)
