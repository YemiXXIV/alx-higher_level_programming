#!/usr/bin/python3

"""

Module of a class representing BaseGeometry

"""


class BaseGeometry:
    """
    class of geometry
    """
    def area(self):
        """
        Method to raise an exception indicating area()
        is not implemented
        """
        raise Exception("area() is not implemented")
