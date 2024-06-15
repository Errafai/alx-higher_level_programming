#!/usr/bin/python3
"""square class module."""


class Square:
    """the square classs with the attribute size."""

    def __init__(self, size=0, position=(0, 0)):
        """initialize the size of the square.

        Args:
            size (int): the size of the square.
            position (tuple): a tuple of tow integers
        """
        self.__size = size
        self.__position = position

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
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def positon(self, position):
        """set the position"""
        if not isinstance(position, tuple) or len(postion) != 2 or \
           not all(isinstance(item, int) for item in position) or \
           not all(item >=0 for item in position):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def my_print(self):
        """print the square using size."""
        if self.__size == 0:
            print()
            return
        print('\n'* self.__position[1] , end="")
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
