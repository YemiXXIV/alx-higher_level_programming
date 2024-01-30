#!/usr/bin/python3
"""

Module that divides an element by a number

"""


def matrix_divided(matrix, div):
    """
    Matrix divider
    """
    if isinstance(div, int) == 0 and isinstance(div, float) == 0:
        raise TypeError("div must be a number")
    new_matrix = []
    i = 0
    for row in matrix:
        temp = []
        for element in row:
            if isinstance(element, int) or isinstance(element, float):
                temp.append(round((element / div), 2))
            else:
                j = "matrix must be a matrix (list of lists)"
                k = " of integers/floats"
                raise TypeError(j + k)
        if i != 0:
            if i != len(row):
                j = "Each row of the matrix"
                k = " must have the same size"
                raise TypeError(j + k)
        i = len(row)
        new_matrix.append(temp)
    return new_matrix
