#!/usr/bin/python3
"""a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    Repo = sys.argv[1]
    Owner = sys.argv[2]
    url = f"https://api.github.com/repos/{Owner}/{Repo}/commits"
    response = requests.get(url=url)
    if response.status_code == 200:
        json_data = response.json()
        idx = 0
        for dic in json_data:
            if idx >= 10:
                break
            idx += 1
            print(f"{dic['sha']}: {dic['commit']['author']['name']}")
    else:
        print(None)
