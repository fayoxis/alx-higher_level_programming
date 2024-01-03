#!/usr/bin/python3

def magic_calculation(w, x, y):
    if w < x:
        result = y
    elif y > x:
        result = w + x
    else:
        result = w * x - y

    return result
