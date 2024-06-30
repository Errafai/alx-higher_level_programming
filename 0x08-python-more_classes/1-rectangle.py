#!/usr/bin/python3
"""adding the width and the hight to the rectangle"""


class Rectangle:
    """this is a rectangle class
    Attributes:
        width (int): the with of the rectangle
        hight (int): the hight of the rectangle

    """
    def __init__(self, width=0, hight=0):
        """initialising the with and hight of the rectangle

            Args:
                width (int): the width of the rectangle
                hight (int): the hight of the rectangle
        """
        self.width = width
        self.hight = hight

    @property
    def width(self):
        """getter function for the width
        Returns:
            int: the value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter function of the width
        Args:
            value (int): the value to be set in the width
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def hight(self):
        """getter function for the hight
        Returns:
        int: the value of the hight
        """
        return self.__hight

    @hight.setter
    def hight(self, value):
        """setter function of the hight
        Args:
            value (int): the value to be set in the hight
        Raises:
            TypeError: if the hight is not an integer
            ValueError: if the value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("hight must be an integer")
        if value <= 0:
            raise ValueError("hight must be >= 0")
        self.__hight = value
