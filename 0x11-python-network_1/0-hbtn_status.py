#!/usr/bin/python3
"here is the fetches https://alx-intranet.hbtn.io/status"
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.alxswe.com/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
