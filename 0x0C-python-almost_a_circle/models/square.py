#!/usr/bin/python3

"""
Module for Square class

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
