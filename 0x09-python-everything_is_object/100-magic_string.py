#!/usr/bin/python3

class MagicString:
    def __init__(self):
        self.n = 0

    def magic_string(self):
        self.n += 1
        return ("BestSchool, " * (self.n - 1) + "BestSchool")

magic_string = MagicString().magic_string
