#!/usr/bin/python3
"""Defines a function that prints a text file to stdout"""


def read_file(filename=""):
    """Reads a text file encoding by `UTF8` and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
