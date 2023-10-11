#!/usr/bin/python3
"""
Defines a function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text `new_string` to a file, after each line
    containing a specific string `search_string`.
    """
    temp = ""
    with open(filename, 'r') as f_read:
        for line in f_read:
            temp += line
            if search_string in line:
                temp += new_string

    with open(filename, 'w') as f_write:
        f_write.write(temp)
