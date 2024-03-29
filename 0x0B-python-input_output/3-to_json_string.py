#!/usr/bin/python3

"""

A function that returns the JSON representation of an object(string)

"""
import json


def to_json_string(my_obj):
    """
    Method to return the JSON representation of an object
    """
    return json.dumps(my_obj)
