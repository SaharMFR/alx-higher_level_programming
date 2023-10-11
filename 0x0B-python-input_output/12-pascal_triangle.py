#!/usr/bin/python3
"""Defines a function creates the Pascal's triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of `n`.
    """
    p_triangle = []
    if n > 0:
        p_triangle.append([1])
        for i in range(n - 1):
            last = p_triangle[-1]
            temp = [1]
            for j in range(len(last) - 1):
                temp.append(last[j] + last[j + 1])
            temp.append(1)
            p_triangle.append(temp)

    return p_triangle
