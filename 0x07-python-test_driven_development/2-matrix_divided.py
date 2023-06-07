#!/usr/bin/python3
"""
A function that divides all elements of a matrix
Arguments:
    matrix: A list of lists containing integers or floats numbers
    div: A number to divide the matrix elements by
"""


def matrix_divided(matrix, div):
    """
    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats
    ach row of the matrix must be of the same size,
    ZeroDivisionError: if div is equal to 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(r, list) for r in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [n for r in matrix for n in r])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(r) == len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in lis] for lis in matrix]
