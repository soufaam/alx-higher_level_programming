#!/usr/bin/python3
"""a Python script that takes in a URL, sends
a request to the URL and displays the body of
the response (decoded in utf-8)."""
from urllib import request, parse
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            decoded = response.read().decode('utf-8')
            print(f"{decoded}")
    except HTTPError as err:
        print(f"Error code: {err.code}")
