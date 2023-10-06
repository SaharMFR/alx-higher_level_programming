#!/usr/bin/python3
"""Defines a function to print a square"""


def print_square(size):
    """
    Prints a square with the character `#`.

    Args:
        size: the length of the side of the square.

    Raises:
        TypeError: if `size` is not integer or
            float and less than zero.
        ValueError: if `size` is less than 0.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
