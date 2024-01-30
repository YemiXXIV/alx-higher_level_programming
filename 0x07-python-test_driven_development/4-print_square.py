#!/usr/bin/python3
"""
Print Squares
"""


def print_square(size):
    """
    prints square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
