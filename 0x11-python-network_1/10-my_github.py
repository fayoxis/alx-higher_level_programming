#!/usr/bin/python3
"""this script takes your GitHub credentials (username and password)
then uses the GitHub API to display your id.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Set the API endpoint URL
    api_url = "https://api.github.com/user"
    user_name = sys.argv[1]
    user_pass = sys.argv[2]
    response = requests.get(api_url, auth=HTTPBasicAuth(user_name, user_pass))
    json_data = response.json()
    print(json_data.get("id"))
