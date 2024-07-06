#!/usr/bin/python3
"""this module contain the empty class ``BaseGeometry``"""


class BaseGeometry:
    """this represent the class BaseGeometry"""

    def area(self):
        """this function raise an exception of area"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """check if value is valide
        Args:
            name (srt): the name of the value
            value (int): the value
        Raises:
            ValueError: if the value is less or equal to 0
            TypeError: if the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """the present the rectangle class
    Attributes:
        height (int): a private attr present the height of rectangle
        width (int): a private attr present the width of rectangle
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """use this format [Rectangle] <width>/<height> when printing"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ return the areat of a rectangle"""
        return self.__height * self.__width
