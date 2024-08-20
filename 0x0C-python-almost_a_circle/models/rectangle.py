#!/usr/bin/python3
"""this module contain the rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represent the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this function initialize the Rectangle instance

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the position of the rectangle in the x axis
            y (int): the position of the rectangle in the y axis
            id (int): the id of the created shape
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def y(self):
        """get the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    @property
    def x(self):
        """get the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):

        if not isinstance(x, int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle in the screen using the charctar `#`"""

        print("\n" * self.__y, end="")

        for i in range(self.__height):
            print(self.__x * " ", end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """update the value of all attributes"""
        i = 0
        for key in self.__dict__:
            if i == len(args) or len(args) == 0:
                break
            self.__dict__[key] = args[i]
            i += 1
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """represent the rectange informations"""
        rectangle = ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
        return rectangle
