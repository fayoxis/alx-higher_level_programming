#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
digit = abs(number) % 10

if number < 0:
    digit = -digit

output = f"Last digit of {number:d} is {digit:d} and is "

if digit > 5:
    output += "greater than 5"
elif digit == 0:
    output += "0"
else:
    output += "less than 6 and not 0"

print(output)
