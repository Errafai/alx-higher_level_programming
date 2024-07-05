#!/usr/bin/python3
"""this module contains the function ``inherits_from()``"""


def inherits_from(obj, a_class):
    """check if the obj is inherits from a_class or not"""
    return (
            isinstance(obj, a_class) and
            issubclass(obj.__class__, a_class) and
            obj.__class__ != a_class
    )
