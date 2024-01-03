#!/usr/bin/python3

def get_last_digit(number):
    result = abs(number) % 10
    print(result, end="")
    return result
