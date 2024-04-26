#!/usr/bin/python3
"""
the script will takes in a URL, sends a request to the URL
then displays the body of the response (decoded in utf-8).
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
