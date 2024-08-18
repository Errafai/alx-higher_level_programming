#!/usr/bin/python3
"""define a function that print a square"""


def print_square(size):
    """print a square based on the size argumant
    and using the character `#`

    Args:
        size (int): the size of the square
    Raises:
        TypeError: if size is not and integer
                   if size is a float and is less than 0
        ValueError: if size is negative
    """

    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")
    i = 0
    for i in range(size):
        print("#" * size)
