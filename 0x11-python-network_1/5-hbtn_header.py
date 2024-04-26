#!/usr/bin/python3
"""
the script will takes in a URL, sends a request to the URL then displays
values of the X-Request-Id variable
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get(argv[1])
    print(response.headers.get('x-request-id'))
