#!/usr/bin/python3
"""
this script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            decoded_response = response.read().decode("ascii")
            print(decoded_response)
    except urllib.error.HTTPError as e:
        error_code = e.code
        print("Error code: {}".format(error_code))
