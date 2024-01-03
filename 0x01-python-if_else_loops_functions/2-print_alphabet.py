#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

output = ""

for letter in range(97, 123):
    output += "{}".format(chr(letter))

print(output, end="")
