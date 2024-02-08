#!/usr/bin/python3

"""

A class that defines a rectangle by its width and height

"""


class Rectangle:
    """
    Defining a rectangle by its width and height
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the preimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Returns a string representation of rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]
