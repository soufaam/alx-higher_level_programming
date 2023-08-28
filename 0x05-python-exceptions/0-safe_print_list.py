#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for idx in range(x):
            print("{}".format(my_list[idx]), end='')
            number += 1
        print()
    except IndexError:
        print()
        return number
    return number
