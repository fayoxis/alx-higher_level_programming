#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
else:
    operator = argv[2]
    if operator in ['+', '-', '*', '/']:
        func = {'+': add, '-': sub, '*': mul, '/': div}[operator]
        result = func(int(argv[1]), int(argv[3]))
        print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), operator, int(argv[3]), result))
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
