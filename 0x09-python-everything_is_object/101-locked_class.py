#!/usr/bin/python3
"""Defines a LockedClass"""


class LockedClass:
    """
    Prevents the user from dynamically creating
    new instance attributes, except `first_name`
    """

    __slots__ = ['first_name']
