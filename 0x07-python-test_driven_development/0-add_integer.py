#!/usr/bin/python3
def add_integer(a, b=98):
    """ return the addition of to integers and raise a typerror
        if the args are not integers
        Args:
            a (int): the first value
            b (int): the second value with 98 as initial value
        Return:
             the addiction of a and b (a + b)
        Raise:
            TypeError: if a or b are not integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
