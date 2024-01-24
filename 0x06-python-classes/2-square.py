#!/usr/bin/python3
"""
Defines a class named square with a private instance

"""


class Square:
    """contains a private instance attribute"""
    def __init__(self, size=0):
        """function to initialize size"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
