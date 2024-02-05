#!/usr/bin/python3

"""

Function to check if an object is an instance of a class inherited

"""


def inherits_from(obj, a_class):
    """
    Method to check if an object is an instance of a class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
