#!/usr/bin/python3
import random
number = random. randint(-10000, 10000)
if number < 0:
    last_digit = number * -1
    n = last_digit % 10
    print(f"Last digit of {number} is {n * -1} and is less than 6 and not 0")
elif number == 0 or number > 0:
    n = number % 10
    if n > 5:
        print(f"Last digit of {number} is {n} and is greater than 5")
    elif n == 0:
        print(f"Last digit of {number} is {n} and is 0")
    elif n < 6 and not 0:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
