#!/usr/bin/python3
"""Defines a class `MyList` that inherits from `list`"""


class MyList(list):
    """Has some added features"""
    def print_sorted(self):
        """Prints the list sorted (ascending order)"""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
