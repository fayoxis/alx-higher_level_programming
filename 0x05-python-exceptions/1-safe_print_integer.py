#!/usr/bin/python3
def safe_print_integer(value):
    try:
        output = "{:d}".format(value)
        print(output)
        return True
    except (TypeError, ValueError):
        return False
