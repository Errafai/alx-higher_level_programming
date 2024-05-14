#!/usr/bin/python3

def safe_print_division(a, b):
    d = float(0)
    try:
        d = a / b
    except (ZeroDivisionError, TypeError):
        d = None
    finally:
        print("Inside result: {}".format(d))
        return d
