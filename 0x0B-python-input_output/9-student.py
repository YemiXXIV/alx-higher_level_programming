#!/usr/bin/python3

"""

A class student that defines a student

"""


class Student:
    """
    Method to define a class named Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes an instance of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary containing the attributes of
        the student instance
        """
        return self.__dict__
