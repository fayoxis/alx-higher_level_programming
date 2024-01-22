#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
