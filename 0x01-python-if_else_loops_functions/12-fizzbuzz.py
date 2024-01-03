#!/usr/bin/python3


def fizzbuzz():
    output = []
    number = 1
    while number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            output.append("FizzBuzz")
        elif number % 3 == 0:
            output.append("Fizz")
        elif number % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(number))
        number += 1
    return ' '.join(output)
