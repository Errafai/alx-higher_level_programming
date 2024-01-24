#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = set(my_list)
    ss = 0
    for i in s:
        ss = ss + i
    return ss
