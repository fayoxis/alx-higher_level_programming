#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    num1 = 1
    num2 = 2
    output = add(num1, num2)
    print("{} + {} = {}".format(num1, num2, output))
