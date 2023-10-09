#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
