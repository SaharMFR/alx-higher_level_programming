#!/usr/bin/python3
"""Defines an addition function"""


def add_integer(a, b=98):
    """Returns the addition of 2 integer numbers.

    Args:
        a: first number.
        b: second number.

    The numbers are casted to integers
    if they are floats (before addition).

    Raises:
        TypeError: if either of the numbers not integer or float.
    """
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError('a must be an integer')
    elif (type(b) is not int) and (type(b) is not float):
        raise TypeError('b must be an integer')
    else:
        return int(int(a) + int(b))
