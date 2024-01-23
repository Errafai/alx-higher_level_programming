#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            str = "FizzBuzz"
        elif i % 3 == 0:
            str = "Fizz"
        elif i % 5 == 0:
            str = "Buzz"
        else:
            str = i
        print(str, end=" ")
