#!/usr/bin/python3
"""this module contain the empty class ``BaseGeometry``"""


class BaseGeometry:
    """this represent the class BaseGeometry"""

   # def __init__(self, name, value):
    #    self.name = name
     #   self.value = value

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

