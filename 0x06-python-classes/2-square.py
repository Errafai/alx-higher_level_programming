#!/usr/bin/python3
"""square class module"""

class Square:
    def __init__(self, size):

        if isinstance(size, int):
            raise ValueError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
