#!/usr/bin/python3
"""this module contain a function that split strings"""

def text_indentation(text):
    """this function split the text if he finds these delimeters `.`, `?`
    and `:`, and replace it with 2 new lines

    Args:
        text (str): the string to be split it

    Raises:
        TypeError: if the text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    j = 0
    while j < len(text):
        if text[j] in ".?:":
            print(text[j] + "\n")
            j += 1
            continue
        if text[j] == ' ' and text[j - 1] in ".?:":
            j += 1
            continue
        print(text[j], end="")
        j += 1
