#!/usr/bin/python3
"""Defines a function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """
    Appends `text` at the end of the text file `filename`.
    `UTF8` endcoding.
    Returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
