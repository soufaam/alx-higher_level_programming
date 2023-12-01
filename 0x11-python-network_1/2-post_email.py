#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of
the response (decoded in utf-8)"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    dic = {'email': sys.argv[2]}
    data = parse.urlencode(dic).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as response:
        decoded = response.read().decode('utf-8')
        print(f"{decoded}")
