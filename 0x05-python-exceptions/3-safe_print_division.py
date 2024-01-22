#!/usr/bin/python3
from __future__ import print_function


def safe_print_division(a, b):
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
