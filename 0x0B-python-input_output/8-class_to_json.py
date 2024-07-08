#!/usr/bin/python3
"""represent the function class_to_json() that turn an
instance of a class to json string"""


import json


def class_to_json(obj):
    """this function usese the __dict__ atttibute to
    convert the obj to json string"""

    return json.dumps(obj.__dict__)
