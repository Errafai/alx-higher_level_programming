#!/usr/bin/python3
def no_c(my_string):
    a = [i for i in my_string if i not in ("c", "C")]
    return "".join(a)
