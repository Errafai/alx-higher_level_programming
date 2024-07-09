#!/usr/bin/python3
import sys
i = 0
a = 0
list3 = []
for line in sys.stdin:
    string = line.split()
    list1 = string[-2:]
    a += int(list1[-1])
    list3.append(list1[0])
    if (i % 10 == 0 and i != 0):
        dict1 = {key: list3.count(key) for key in list3}
        print("File size: {}".format(a))
        dict1 = {k: dict1[k] for k in sorted(dict1)}
        for key, value in dict1.items():
            print("{}: {}".format(key, value))
        dict1 = {}
        list3 = []
    i += 1
