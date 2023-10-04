#!/usr/bin/python3
"""Defines a function to devide matrix by number"""


def matrix_divided(matrix, div):
    """
    Devides all elements of a `matrix` by the number `div`
    rounded to 2 decimal places.

    Args:
        matrix: the matirx to devide.
        div: the number to devide by.

    Raises:
        TypeError: when any element of the matirx and `div`
            is not integer or float or when not all the rows
            of the matrix are of the same size.
        ZeroDivisionError: when `div` is equal to 0.

    Returns a new matrix
    """
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError('matrix must be a matrix (list of lists) \
                of integers/floats')
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix '
                    'must have the same size')
        new_matrix.append([])
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) is not int \
                    and type(matrix[i][j]) is not float:
                raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
