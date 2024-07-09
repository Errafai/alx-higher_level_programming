#!/usr/bin/python3
"""this module reads the input in stdin and use those information
to pring the file sizes and status code the number of reptation of
status code"""


import sys
i = 0
a = 0
list3 = []
for line in sys.stdin:
    string = line.split()
    list1 = string[-2:]
    a += int(list1[-1])
    list3.append(list1[0])
    if (i % 10 == 9):
        dict1 = {key: list3.count(key) for key in list3}
        print("File size: {:d}".format(int(a)))
        dict1 = {k: dict1[k] for k in sorted(dict1)}
        for key, value in dict1.items():
            print("{:d}: {:d}".format(int(key), int(value)))
        dict1 = {}
        list3 = []
    i += 1
