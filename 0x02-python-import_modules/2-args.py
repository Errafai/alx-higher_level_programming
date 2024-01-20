#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    j = len(av)
    if j == 1:
        print("0 arguments.")
    elif j == 2:
        print("1 argument:")
        print("1: {}".format(av[1]))
    else:
        print("{} arguments:".format(j-1))
        for i in range(1, j):
            print("{}: {}".format(i, av[i]))
