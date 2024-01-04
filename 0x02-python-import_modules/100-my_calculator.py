#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
if len(sys.argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

if operator == '+':
        result = add(a, b)
elif operator == '-':
        result = sub(a, b)
elif operator == '*':
        result = mul(a, b)
elif operator == '/':
        result = div(a, b)
else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))

if __name__ == "__main__":
    main()
