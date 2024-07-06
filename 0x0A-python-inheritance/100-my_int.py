#!/usr/bin/python3
"""my_Int is a subclass of int"""


class MyInt(int):
    """reprsent the subclass MyInt"""

    def __eq__(self, other):
        """invert the == sign in my_int"""
        if isinstance(other, int):
            return other is self
        return False

    def __ne__(self, other):
        """invert the != signe in my_int"""
        if isinstance(other, int):
            return other is not self
        return False
