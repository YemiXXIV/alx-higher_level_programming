#!/usr/bin/python3

"""

A class representing basic geometry

"""


class BaseGeometry:
    """
    Class representing geometry
    """
    def area(self):
        """
        Raise an exception indicating area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer
        and greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
