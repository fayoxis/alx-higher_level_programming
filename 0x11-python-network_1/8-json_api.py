#!/usr/bin/python3
"""
this script will takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    query = argv[1] if len(argv) > 1 else ""
    payload = {"q": query}
    response = requests.post(url, data=payload)

    try:
        json_output = response.json()
        if not json_output:
            print("No result")
        else:
            user_id = json_output.get("id")
            user_name = json_output.get("name")
            print(f"[{user_id}] {user_name}")
    except ValueError:
        print("Not a valid JSON")
