#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size: The size of the new Square (int).
            position: The position of the new Square (tuple)."""
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """To retrieve the private instance attribute 'size'."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """To set the private instance attribute 'size'."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """To retrieve the private instance attribute 'position'."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """To set the private instance attribute 'position'."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(' ', end='') for j in range(0, self.__position[0])]
                [print('#', end='') for k in range(0, self.__size)]
                print()
        else:
            print()
