#!/usr/bin/python3

"""

A function that returns a list of integers represeenting
the pascal's triangle of n

"""


def pascal_triangle(n):
    """
    Method to create pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            if j== i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i -1][j])
        triangle.append(row)

    return triangle
