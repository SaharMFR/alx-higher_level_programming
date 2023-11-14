#!/usr/bin/python3
"""Defines a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square that inherits from `Rectangle`"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns info about the square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.size))

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, s):
        if type(s) is not int:
            raise TypeError('width must be an integer')
        if s <= 0:
            raise ValueError('width must be > 0')
        self.__width = s
        self.__height = s

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args and len(args):
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a `Square`"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
