#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [3, 6, 9],
        [12, 15, 18]
    ]
print(matrix_divided(matrix, 3))

matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
print(matrix_divided(matrix, 3))

matrix = [
        [1.1, -2.2, 3.3],
        [4.4, 5.5, -6.6]
    ]
print(matrix_divided(matrix, 3))

matrix = [
        [1, -2.2, 3, 4.4, 5],
        [-6.6, 7.00, 8, 9.999, 10]
    ]
print(matrix_divided(matrix, 3))

matrix = "string"
print(matrix_divided(matrix, 2))
