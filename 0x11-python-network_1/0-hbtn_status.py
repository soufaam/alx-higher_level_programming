#!/usr/bin/python3
"""This  a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as data:
        Response = data.read()
        print("Body response:")
        print(f"\t- type: {Response.__class__}")
        print(f"\t- content: {Response}")
        print(f"\t- utf8 content: {Response.decode('utf-8')}")
