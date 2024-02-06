#!/usr/bin/python3

"""

A function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """
    Method to write a string to a text file
    Return: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
