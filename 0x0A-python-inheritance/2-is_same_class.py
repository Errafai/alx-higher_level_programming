#!/usr/bin/python3
"""this module conatains the function ``is_same_class()``"""


def is_same_class(obj, a_class):
    """return false if obj is the same as a_class
    or True if the obj is the same as a_class"""
    return isinstance(obj, a_class) and issubclass(obj, a_class)
