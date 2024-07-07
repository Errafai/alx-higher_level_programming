#!/usr/bin/python3
"""repsent a function to load json string from a file"""


import json


def load_from_json_file(filename):
    """this load a json file content and
    return an object"""

    with open(filename, "r", encoding="utf-8") as j:
        return json.load(j)
