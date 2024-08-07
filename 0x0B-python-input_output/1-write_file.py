#!/usr/bin/python3
"""this module contain the write_file() function"""


def write_file(filename="", text=""):
    """write the text on a file
    return none

    Args:
        filename (str): the name of the file
        text (str): the text wanna write
    Returns:
        int: the number of character writen in the file
    """
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
