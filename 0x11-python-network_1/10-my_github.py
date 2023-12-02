#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
from requests.auth import HTTPBasicAuth
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    url = f"https://api.github.com/user"
    login = requests.get(url=url, auth=HTTPBasicAuth(username, passwd))
    if login.status_code == 200:
        print(login.json()['id'])
    else:
        print(None)
