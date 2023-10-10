#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a `text` to the text file `filename` encoding by `UTF8`.
    Returns the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
