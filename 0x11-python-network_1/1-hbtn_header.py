#!/usr/bin/python3
"""This is a Python script that takes in a URL,
sends a request to the URL and displays the value of
he X-Request-Id variable found in the header
of the response."""
from urllib.request import urlopen
import sys


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as data:
        headers = data.getheaders()
        for item in headers:
            if 'X-Request-Id' in item:
                print(item[1])
