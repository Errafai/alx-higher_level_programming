#!/usr/bin/python3
"""represent the function class_to_json() that turn an
instance of a class to json string"""


def class_to_json(obj):
    """this function usese the __dict__ atttibute to
    convert the obj to json string"""

    return obj.__dict__
