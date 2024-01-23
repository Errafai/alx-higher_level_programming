#!/usr/bin/python3
def print_last_digit(number):
    m = number if number > 0 else -number
    print(m % 10, end="")
    return m % 10
