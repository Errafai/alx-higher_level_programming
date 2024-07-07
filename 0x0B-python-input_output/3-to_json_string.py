#!/usr/bin/python3
"""this module contains the function ``to_json_string()``"""


import json


def to_json_string(my_obj):
    """tranform the object to a json string repsentation

    Args:
        my_obj (object):  the object to be coverting
    Returns:
        str: a json repsentation of the object
    """
    return json.dumps(my_obj)
