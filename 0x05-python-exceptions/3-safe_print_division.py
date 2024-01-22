#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print(f"Inside result: {res}")
    return res
