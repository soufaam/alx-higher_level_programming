#!/usr/bin/python3
import sys
import marshal
with open("hidden_4.pyc", "rb") as f:
    code = marshal.load(f)
    print(code)