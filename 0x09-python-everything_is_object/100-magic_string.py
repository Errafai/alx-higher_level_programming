#!/usr/bin/python3
def magic_string(counter=[0]):
    counter[0] += 1
    return "BestSchool, " * (counter[0] - 1) + "BestSchool"
