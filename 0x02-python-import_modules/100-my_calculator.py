#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def calculate_result(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        return None

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    
    result = calculate_result(a, operator, b)
    if result is None:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
    
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
