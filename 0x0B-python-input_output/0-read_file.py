#!/usr/bin/python3

"""

A function that reads a text file and prints it to stdout.

"""

def read_file(filename=""):
    """
    Method to read a text file and print it to stdout
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
