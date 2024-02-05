#!/usr/bin/python3

"""

Function that checks if an object returns exactly an instance of a class

"""


def is_same_class(obj, a_class):
    """
    Method to return if object is an instance of the specified class or not
    """
    return type(obj) is a_class
