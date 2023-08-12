#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    for item in range(0, len(my_list)):
        if idx == item:
            copy_list.append(element)
        else:
            copy_list.append(my_list[item])
    return copy_list
