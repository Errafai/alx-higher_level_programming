#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    from calculator_1 import add, sub, mul, div
    if len(av) != 4:
        print("Usage ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if av[2]  not in ["+", "-", '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        av[1] = int(av[1])
        av[3] = int(av[3])
        if av[2] == "+":
            print("{} {} {} = {}".format(av[1], av[2], av[3], add(av[1], av[3])))
        elif av[2] == "-":
            print("{} {} {} = {}".format(av[1], av[2], av[3], sub(av[1], av[3])))
        elif av[2] == "*":
            print("{} {} {} = {}".format(av[1], av[2], av[3], mul(av[1], av[3])))
        else:
            print("{} {} {} = {}".format(av[1], av[2], av[3], div(av[1], av[3])))
