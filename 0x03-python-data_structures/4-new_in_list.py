#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = [i for i in my_list]
    if idx < 0 or idx >= len(my_list):
        return a
    a[idx] = element
    return a
