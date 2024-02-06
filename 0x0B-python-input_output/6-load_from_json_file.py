#!/usr/bin/python3

"""

A function that creates an object from a JSON file

"""
import json


def load_from_json_file(filename):
    """
    Method to create an object from a JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)
