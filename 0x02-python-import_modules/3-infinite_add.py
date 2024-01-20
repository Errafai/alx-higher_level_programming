#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as a
    s = 0
    for i in a[1:]:
        s += int(i)
    print(s)
