#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

argc = len(argv) - 1

if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)
else:
    operator = argv[2]
    operands = (int(argv[1]), int(argv[3]))

    if operator == '+':
        result = add(*operands)
    elif operator == '-':
        result = sub(*operands)
    elif operator == '*':
        result = mul(*operands)
    elif operator == '/':
        result = div(*operands)

    print("{:d} {:s} {:d} = {:d}".format(*operands, result))
