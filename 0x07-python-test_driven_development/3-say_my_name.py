#!/usr/bin/python3
"""
Defines a function to say:
`My name is ` + first_name + ` ` + last_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints (`My name is ` + first_name + ` ` + last_name)

    Args:
        first_name: the first name.
        last_name: the last name (empty string by default)

    Raises:
        TypeError: when any one of the two arguments is not string.
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
