#!/usr/bin/python3
"""this file contains the read_file() method"""


def read_file(filename=""):
    """read the file and print the content of the file
    to the output

    Args:
        filename (str): the name of the file
    """

    with open(filename, encoding="uft-8") as f:
        print(f.read())
