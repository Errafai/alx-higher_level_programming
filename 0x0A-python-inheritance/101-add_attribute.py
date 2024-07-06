#!/usr/bin/python3
"""contains the add_attribute"""


def add_attribute(obj, attr, value):
    """adds an attribue to the obj class

    Args:
        obj (class): the class to add attribute
        attr (str): the name of attribute
        value (object): the value of the attr
    Raises:
        TypeError: if we can't add the attr
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
