#!/usr/bin/python3
"""
this script will fetches https://alx-intranet.hbtn.io/status.
"""
if __name__ == "__main__":
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(
        type(response.text), response.text))
