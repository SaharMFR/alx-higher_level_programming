#!/usr/bin/python3
"""Defines class MyInt that inherits from int"""


class MyInt(int):
    """Rebel class (== and != are inverted)"""

    def __eq__(self, value):
        return (self.real != value)

    def __ne__(self, value):
        return (self.real == value)
