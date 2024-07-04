#!/usr/bin/python3
def lookup(obj):
    li = []
    for i in obj.__dict__:
        li.append(i)
    return li
