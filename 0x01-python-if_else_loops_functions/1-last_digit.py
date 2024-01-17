#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
n = number % 10
m = n
if number < 0:
    n = n - 10
    m = -n
if 0 < m < 6:
    str = "and is less than 6 and not 0"
elif m > 5:
    str = "and is greater than 5"
else:
    str = "and is 0"
print(f"Last digit of {number} is {n} {str}")
