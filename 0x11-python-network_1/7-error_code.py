#!/usr/bin/python3
"""
the script will takes in a URL, sends a request to the URL
then displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        response = get(argv[1])
        response.raise_for_status()
    except:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
