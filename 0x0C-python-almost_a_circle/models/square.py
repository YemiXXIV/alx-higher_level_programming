#!/usr/bin/python3

"""
Module for Square class

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes Square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes of the Square instance
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args[:len(attrs)]):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns string representation of Square instance
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """
        Returns dictionary representation of Square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
