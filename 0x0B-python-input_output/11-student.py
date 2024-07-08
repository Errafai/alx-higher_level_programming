#!/usr/bin/python3
"""this module contains the student class"""


class Student:
    """represent the student module"""

    def __init__(self, first_name, last_name, age):
        """initialize the student class

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation of a Student instance"""

        if attrs is None:
            return self.__dict__
        else:
            rep = {}
            for value in attrs:
                if hasattr(self, value):
                    rep[value] = self.__dict__[value]
            return rep

    def reload_from_json(self, json):
        """change student attribute"""

        for key, value in json.items():
            setattr(self, key, value)
