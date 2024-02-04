#!/usr/bin/python3
"""
trying to make nice documentation.
"""


def matrix_divided(matrix, div):
    mesage_lists = "matrix must be a matrix (list of lists) of integers/floats"
    message_rows = "Each row of the matrix must have the same size"

    """
    matrix: matrix of integers
    """
    if not isinstance(matrix, list):
        raise ValueError(mesage_lists)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(message_rows)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if not isinstance(div, (int, float)):
        raise TimeoutError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
