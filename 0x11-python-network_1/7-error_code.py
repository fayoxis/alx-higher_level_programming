#!/usr/bin/python3
"""
the script will takes in a URL, sends a request to the URL
then displays the body of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        url = argv[1]
        response = get(url)
        response.raise_for_status()
    except IndexError:
        print("Error: No URL provided as command-line argument.")
    except requests.exceptions.RequestException as e:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
