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

    def to_json(self, attrs=None):
        new_dict = self.__dict__
        """
        Retrieves a new dictionary representation of
        the student instance
        """
        if attrs is None:
            return new_dict
        else:
            return {key: new_dict[key] for key in attrs if key in new_dict}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance with values
        from a dict
        """
        for key, value in json.items():
            setattr(self, key, value)
