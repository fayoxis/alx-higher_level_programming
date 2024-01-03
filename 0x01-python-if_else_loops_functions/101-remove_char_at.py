#!/usr/bin/python3

def remove_char_at(string, index):
    if index < 0:
        return string
    return string[:index] + string[index+1:]
