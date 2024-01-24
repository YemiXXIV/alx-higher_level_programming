#!/usr/bin/python3
"""
Defines a class named Square with private instance
"""


class Square:
    """Contains private instance attributes size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using # with position"""
        if self.__size != 0:
            for j in range(self.__position[1]):
                print()
            for k in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
