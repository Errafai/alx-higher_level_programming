#!/usr/bin/python3
"""adding the width and the hight to the rectangle"""


class Rectangle:
    """this is a rectangle class
    Attributes:
        width (int): the with of the rectangle
        hight (int): the hight of the rectangle
        number_of_instances (int): represent the number
                                   of rectangle instances exist
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialising the with and hight of the rectangle

            Args:
                width (int): the width of the rectangle
                hight (int): the hight of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for the hight
        Returns:
        int: the value of the hight
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter function of the height
        Args:
            value (int): the value to be set in the height
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """caluculate the area of the recatangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """return a string thar represent the string"""
        s = str(self.print_symbol)
        rect = [s * self.__width for i in range(self.__height)]
        if self.__width == 0 or self.height == 0:
            return ""
        return "\n".join(rect)

    def __repr__(self):
        """return string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """called when the rectangle is being deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
