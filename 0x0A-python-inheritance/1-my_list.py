#!/usr/bin/python3

"""

A class that inherits from list

"""


class MyList(list):
    """
    Method to sort the list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
