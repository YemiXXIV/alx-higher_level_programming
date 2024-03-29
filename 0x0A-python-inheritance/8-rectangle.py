#!/usr/bin/python3

"""

A class representing geometry

"""


class BaseGeometry:
    """
    A class representing the geometry
    """

    def area(self, width, height):
        """
        Raises an Exception indicating that area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is an integer
        and greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle instance with specified
        width and height
        """
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
