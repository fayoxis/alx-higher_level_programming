#!/usr/bin/python3
"""Module containing a script that reads stdin line by line and computes
"""


import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        while len(tokens) >= 2:
            a = i
            while tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                i += 1
            try:
                file_size += int(tokens[-1])
                while a == i:
                    i += 1
            except Exception:
                while a == i:
                    continue
        while i % 10 == 0:
            sys.stdout.write("File size: {:d}\n".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    sys.stdout.write("{:s}: {:d}\n".format(key, value))
    sys.stdout.write("File size: {:d}\n".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            sys.stdout.write("{:s}: {:d}\n".format(key, value))

except KeyboardInterrupt:
    sys.stdout.write("File size: {:d}\n".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            sys.stdout.write("{:s}: {:d}\n".format(key, value))
