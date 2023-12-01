#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    resp = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        jsonformat = resp.json()
        if jsonformat == {}:
            print("No result")
        else:
            print(f"{jsonformat['id']} {jsonformat['name']}")
    except Exception as exc:
        print("Not a valid JSON")
