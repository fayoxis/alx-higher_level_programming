#!/usr/bin/python3
"""
the script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode("utf-8")
        print(response_data)
