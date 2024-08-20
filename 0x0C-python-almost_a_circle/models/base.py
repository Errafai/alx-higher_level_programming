#!/usr/bin/python3
"""this module define the base class"""


import json

class Base:
    """represent the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """mannaging the id attribute in all future classes
        and to avoid duplicating the same code (by extension, same bugs)
        Args:
            id (int): it is a the id of each instance of the class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """transforming a dictionary into a json string"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)


