#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    for item in range(0, len(my_list)):
        if idx == my_list:
            copy_list[item] = element
        else:
            copy_list[item] = my_list[item]
    return copy_list
