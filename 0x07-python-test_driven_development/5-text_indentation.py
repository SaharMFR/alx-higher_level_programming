#!/usr/bin/python3
"""Defines a function re-write a text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: '.' and '?' and ':'.

    Args:
        text: the text to re-write.

    Raises:
        TypeError: if 'text' is not a string.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print()
                print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
