#!/usr/bin/python3
"""this module contain the append_write() function"""


def append_write(filename="", text=""):
    """append the text to the file
    return none

    Args:
        filename (str): the name of the file
        text (str): the text wanna append
    Returns:
        int: the number of character appendn in the file
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
