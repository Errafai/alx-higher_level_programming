#!/usr/bin/python3
"""this module contain the ``say_my_name`` function """


def say_my_name(first_name, last_name=""):
    """ this function print My name is <first name> <last name>
    with no return just printing

    Args:
        first_name (string): the first name of the person
        last_name (string): the last name of the person

    Raises:
        TypeError: +if the first name is not a string
                   +if the last name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
