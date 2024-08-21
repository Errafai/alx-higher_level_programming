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

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""

        if list_objs is None:
            recs = []
        else:
            recs = [r.to_dictionary() for r in list_objs]

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = Base.to_json_string(recs)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """transform a json string into a list of dict in python"""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create new intance of the cls type and assigne
        attribute that already exist in the dictionary"""

        if cls.__name__ == "Rectangle":
            dummy = cls(34, 2)
        else:
            dummy = cls(3)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """get instances data from a a json file"""

        filename = cls.__name__ + '.json'
        try:
            with open(filename, "r") as file:

                rectangles = file.read()
                rects_list = cls.from_json_string(rectangles)
                new_rects = [cls.create(**r) for r in rects_list]
                return new_rects

        except FileNotFoundError:
            return []
