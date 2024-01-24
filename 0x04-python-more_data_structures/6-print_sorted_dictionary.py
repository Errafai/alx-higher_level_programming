#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictonary = sorted(a_dictionary)
    for x,y in a_dictionary.items():
        print("{}: {}".format(x, y))
