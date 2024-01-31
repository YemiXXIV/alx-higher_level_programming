#!/usr/bin/python3
"""

Class tha prevents dynamic instances creation

"""


class LockedClass:
    def __setattr__(self, name, value):
        """ 
        set attribute method 
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
