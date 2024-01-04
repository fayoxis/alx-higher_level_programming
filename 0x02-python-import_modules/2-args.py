#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arg_count = len(sys.argv) - 1
arg_str = "{:d} argument"

if arg_count == 0:
    arg_str += 's.'
elif arg_count == 1:
    arg_str += ':'
else:
    arg_str += 's:'

print(arg_str.format(arg_count))

i = 0

for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
