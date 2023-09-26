#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializing a new Square.
        Args:
            size: The size of the new Square (int)."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size ** 2)

    @property
    def size(self):
        """To retrieve the private instance attribute 'size'."""
        return self.__size

    @size.setter
    def size(self, value):
        """To set the private instance attribute 'size'."""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
