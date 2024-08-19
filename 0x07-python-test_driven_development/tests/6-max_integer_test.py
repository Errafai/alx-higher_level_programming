#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """this class is used to test the max_integer function
    usting the unittest module"""


    def test_normale(self):
        """testing normale usage of the function"""

        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([2, -2, 0, 189, -3]), 189)

    def test_edge(self):
        """testing edge cases like empty list or list contain one element
        etc..
        """

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([2, 2, 2, 2, 2, 2]), 2)

    def test_special(self):
        """ testing special cases where the numbers can float
        or combination of negative numbers
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([2.2, 533.222, 2.22, 22.22]), 533.222)
        self.assertEqual(max_integer([-22,1.22, -23.2, 20]), 20)
        self.assertEqual(max_integer([1e100, 22, 1e10, -1e100]), 1e100)
        self.assertEqual(max_integer(["kdk", "sldk"]), "sldk")
        self.assertEqual(max_integer("sldk"), "s")
    def test_error(self):
        """testing errors handling when passing no argument
        or passing a list of strings etc..."""

        with self.assertRaises(TypeError):
            max_integer(2223)
            max_integer(True)







