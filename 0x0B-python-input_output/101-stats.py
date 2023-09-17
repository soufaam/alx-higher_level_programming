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
    file_size['size'] = 0
    i = 0
    line = sys.stdin.readline()
    if line == '':
        print(f"File size: {file_size['size']}")
    while line != '':
        i += 1
        parsedline = line.split()
        try:
            file_size["size"] += int(parsedline[-1])
        except ValueError:
            line = sys.stdin.readline()
            continue
        if int(parsedline[-2]) not in status_dict.keys():
            status_dict[int(parsedline[-2])] = 1
        else:
            status_dict[int(parsedline[-2])] += 1
        list_of_keys = list(status_dict.keys())
        list_of_keys.sort()
        line = sys.stdin.readline()
        if i >= 10 or line == '':
            i = 0
            print(f"File size: {file_size['size']}")
            if list_of_keys is not None:
                for code in list_of_keys:
                    print(f"{code}: {status_dict[code]}")


if __name__ == "__main__":
    script_parser()
