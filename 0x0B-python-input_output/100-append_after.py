#!/usr/bin/python3
"""this module contains the function ``append_after()``
that append line after a specific line"""


def append_after(filename="", search_string="", new_string=""):
    """append a new string after a each line containing
    specific string.

    Args:
        filename (str): the name of the file
        search_string (str): a specific string to search for
        new_string (str): the new string to append after search_string

    no return just change
    """

    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            if search_string in line:
                lines.insert(i + 1, new_string)
            i += 1
        file.seek(0)
        file.write("".join(lines))
