#!/usr/bin/python3
from sys import argv
import calculator_1

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
    else:
        operator = argv[2]
        func = getattr(calculator_1, operator)
        result = func(int(argv[1]), int(argv[3]))
        print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), operator, int(argv[3]), result))
