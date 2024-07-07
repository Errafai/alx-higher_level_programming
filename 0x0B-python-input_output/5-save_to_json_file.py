#!/usr/bin/python3
"""here we are using the json module to contruct the
function ``save_to_json_file(my_obj, filename)``"""


import json


def save_to_json_file(my_obj, filename):
    """ save the json string in a file using
    the functon dump() in json module

    Args:
        my_obj (object): the object to be tranfered to the file
        filename (str): the name of the file to input the string

    return none
    """
    with open(filename, "w", encoding="utf-8") as j:
        json.dump(my_obj, j)
