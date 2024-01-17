#!/usr/bin/python3
for i in range(0, 100):
    j = 0 if i <= 9 else ""
    print("{}{:d}, ".format(j,i), end="")
    if i == 99:
        print("{}".format(i))
