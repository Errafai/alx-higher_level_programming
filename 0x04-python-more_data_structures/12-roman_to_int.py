#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    for i in roman_string:
            s += roman[i] * (if i in roman)
    return s
