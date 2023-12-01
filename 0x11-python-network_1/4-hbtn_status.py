#!/usr/bin/python3
"""a Python script that fetches
https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    resulta = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f"\t- type: {resulta.text.__class__}")
    print(f"\t- content: {resulta.text}")
