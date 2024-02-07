#!/usr/bin/python3

"""

A function thaat returns dictionary description with simple
data structure for JSON serialization of an object

"""


def class_to_json(obj):
    """
    Returns: The dictionary description for JSON serialization
    of an object
    """
    return obj.__dict__
