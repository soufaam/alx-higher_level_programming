#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    dic_number = {}
    for item in my_list:
        if item not in dic_number.keys():
            sum += item
        dic_number[item] = True
    return sum
