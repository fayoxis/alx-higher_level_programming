#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ArithmeticError):
        result = None
    finally:
        output = "Inside result: {}".format(result)
        print(output)
        return result
