#!/usr/bin/python3
"""square class module."""


class Square:
    """the square classs with the attribute size."""

    def __init__(self, size=0):
        """initialize the size of the square.

        Args:
            size (int): the size of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """calculate the area of the square.

        Return:
            int: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """return the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """edit the size"""
        size.__size = size
