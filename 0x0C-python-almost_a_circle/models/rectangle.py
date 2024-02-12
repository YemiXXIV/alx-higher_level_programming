#!/usr/bin/python3

"""

Module from Rectangle class

"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Prints the rectangle instance with the character '#'
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigns key/value arguments to attributes
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation of Rectangle
        """
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
