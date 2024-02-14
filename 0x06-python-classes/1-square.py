#!/usr/bin/python3
"""the square module"""


class Square:
    """square with the attribute size"""
    def __init__(self, size):
        """the constructor of the class.

        Args:
            size: the size of the square
        """
        self.__size = size
