#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    lenght = len(my_list)
    result = list(map(lambda x, y: x * y, my_list, [number] * lenght))
    return result
