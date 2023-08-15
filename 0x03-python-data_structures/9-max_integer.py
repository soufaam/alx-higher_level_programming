#!/usr/bin/python3
def max_integer(my_list=[]):
    max = -99999999999999
    if my_list == []:
        return None
    for item in my_list:
        if item > max:
            max = item
    return (max)
