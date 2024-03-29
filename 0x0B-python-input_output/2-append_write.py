#!/usr/bin/python3

"""

A function that appends a string to the end of a text file
Returns: The number of characters added

"""


def append_write(filename="", text=""):
    """
    Method to append a string to the end of a text file
    Returns: The number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
