#!/usr/bin/python3
"""this module represnet the function ``magic_string``"""


def magic_string():
    """this function return everytime n * BestSchool"""
    if not hasattr(magic_string,"counter"):
        magic_string.counter = 0
    magic_string.counter += 1

    return "BestSchool, " * (magic_string.counter - 1) + "BestSchool"
