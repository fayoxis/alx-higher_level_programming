#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    result = 0

    if a < b:
        result = add(a, b)
        for i in range(4, 6):
            result = add(result, i)
        return result

    else:
        return sub(a, b)
