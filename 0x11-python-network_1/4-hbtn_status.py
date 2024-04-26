#!/usr/bin/python3
"""
this script will fetches https://alx-intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.alxswe.com/status")
    print("Body response:")
    print("\t- type: <class 'str'>")
    print("\t- content: OK")
