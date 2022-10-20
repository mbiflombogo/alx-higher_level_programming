#!/usr/bin/python3

"""
Module contains function: matrix_divided()
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divide all elements of matrix by div
    Args:
        matrix (list): list of lists
        div (int): divisor
    Returns:
        list: new matrix divided by div
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists)"
            " of integers/floats"
        )
    i = 1
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for rw in matrix:
        if type(rw) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists)"
                " of integers/floats"
            )
        for el in rw:
            if type(el) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )
        while i < len(matrix):
            if len(rw) != len(matrix[i]):
                raise TypeError(
                    "Each row of the matrix"
                    " must have the same size"
                )
            i += 1
    return [[round(el / div, 2) for el in rw] for rw in matrix]
