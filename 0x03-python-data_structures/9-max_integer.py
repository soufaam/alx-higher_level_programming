#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list == []:
        return None
    for item in my_list:
        if item > max:
            max = item
