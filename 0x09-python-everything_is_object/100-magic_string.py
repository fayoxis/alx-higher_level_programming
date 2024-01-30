#!/usr/bin/python3

class MagicString:
    def __init__(self):
        self.n = 0

    def magic_string(self):
        self.n += 1
        return ("BestSchool, " * (self.n - 1) + "BestSchool")

magic = MagicString()
magic_string = magic.magic_string
