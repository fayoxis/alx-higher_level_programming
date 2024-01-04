#!/usr/bin/env python3
import sys
import hidden_4 as hidden

def main():
    if __name__ != "__main__":
        exit()

    for name in dir(hidden):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()
