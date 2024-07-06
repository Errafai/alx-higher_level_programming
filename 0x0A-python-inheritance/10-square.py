#!/usr/bin/python3
"""this module contains the class ``Square``
wish is a subclass of the Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represente the square class"""

    def __init__(self, size):
        """initialize a square

        Args:
            size (int): the size of the square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
