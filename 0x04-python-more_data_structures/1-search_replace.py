#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx in range(len(my_list)):
        if search == my_list[idx]:
            my_list.remove(my_list[idx])
            my_list.insert(idx, replace)
    return my_list
