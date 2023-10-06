#!/usr/bin/python3
"""Defines a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices

    Args:
        m_a (list of lists of int/float): first matrix to be multiplied.
        m_b (list of lists of int/float): second matrix to be multiplied.

    Raises:
        TypeError: If m_a or m_b is not a list
            or if m_a or m_b is not a list of lists
            or if one element of list of lists is not int/float
            or if row of m_a or m_b are not the same size.
        ValueError: If m_a or m_b is empty
            or if m_a and m_b cannot be multiplied.

    Returns:
        The new matrix that resulted of the multiplication.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((type(element) is int) or type(element) is float
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(element) is int or type(element) is float
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        matrix1.append(my_row)

    matrix2 = []
    for row in m_a:
        my_row = []
        for column in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        matrix2.append(my_row)

    return matrix2
