#!/usr/bin/python3
"""
this script will fetches https://alx-intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.alxswe.com/status")
    print("Response body:")
    print("\t- Type: {}".format(type(response.text)))
    print("\t- Content: {}".format(response.text))
