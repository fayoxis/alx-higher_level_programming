#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

i = 0
result = 0
for arg in sys.argv[1:]:
    result += int(arg)

print("{:d}".format(result))
