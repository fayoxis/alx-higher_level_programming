#!/usr/bin/python3

i = 0
output = ""
for c in range(ord('z'), ord('a') - 1, -1):
    output += "{}".format(chr(c - i))
    i = 32 if i == 0 else 0
print(output, end="")
