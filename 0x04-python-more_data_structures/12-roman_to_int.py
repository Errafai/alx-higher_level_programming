#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    ss = len(roman_string)
    for i in range(ss):
        c = r[roman_string[i]] * (roman_string[i] in r)
        if i < ss - 1 and r[roman_string[i]] < r[roman_string[i + 1]]:
            s -= c
        else:
            s += c
    return s
