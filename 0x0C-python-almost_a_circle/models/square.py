#!/usr/bin/python3
"""this module contian the square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represent the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square class

        Args:
            size (int): the size of the square
            x (int): the position of the square in the x axis (spaces)
            y (int): the position of the square in the y axis (newlines)
            id (int): the id of the created square
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """retpresent the square class infomations"""

        square = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
        return square
