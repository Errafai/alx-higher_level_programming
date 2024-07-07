#!/usr/bin/python3
"""this module uses the json module to implement the
funcion ``from_json_string(my_str)``"""


import json


def from_json_string(my_str):
    """transform a json string into a python object

    Args:
        my_str (str): the string to be transformed
    Returns:
        object: the object that repsent the value
                of the string
    """
    return json.loads(my_str)
