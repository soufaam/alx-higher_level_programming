#!/usr/bin/python3
""" This is a decription of this module .
this module contains append_after function that takes myobject
as parameter
"""

import sys


def script_parser():
    """script parser fhnction"""

    status_dict = {}
    file_size = {}
    i = 0
    line = sys.stdin.readline()
    while line != -1:
        i += 1
        parsedline = line.split()
        if "size" not in file_size.keys():
            file_size["size"] = int(parsedline[-1])
        else:
            file_size["size"] += int(parsedline[-1])
        if int(parsedline[-2]) not in status_dict.keys():
            status_dict[int(parsedline[-2])] = 1
        else:
            status_dict[int(parsedline[-2])] += 1
        list_of_keys = list(status_dict.keys())
        list_of_keys.sort()
        print(f"File size: {file_size['size']}")
        if list_of_keys is not None:
            for code in list_of_keys:
                print(f"{code}: {status_dict[code]}")
        line = sys.stdin.readline()


if __name__ == "__main__":
    script_parser()
