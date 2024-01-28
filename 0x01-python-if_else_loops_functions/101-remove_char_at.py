#!/usr/bin/python3
def remove_char_at(str, n):

    str1 = ""
    for i in range(len(str)):
        str1 += str[i] if i != n else ""
    return str1
