#!/usr/bin/python3
""" This is a decription of this module .
this module contains save_to_json_file function that takes myobject
as parameter
def save_to_json_file(my_obj, filename):
def load_from_json_file(filename):
"""
from json import load, JSONDecodeError
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'
argv_list = []
try:
    with open(filename, "r+") as file:
        data = load_from_json_file(filename)
except FileNotFoundError:
    with open(filename, "w+") as file:
        try:
            data = load_from_json_file(filename)
        except JSONDecodeError:
            data = []
except JSONDecodeError:
    data = []
for i in range(1, len(sys.argv)):
    if data == []:
        data.append(sys.argv[i])
        save_to_json_file(data, filename)
    else:
        data = load_from_json_file(filename)
        data.append(sys.argv[i])
        save_to_json_file(data, filename)
        data = load_from_json_file(filename)
