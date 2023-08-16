#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idx in range(len(my_list)):
        if search == my_list[idx]:
            new_list.append(replace)
        else:
            new_list.append(my_list[idx])
    return new_list
