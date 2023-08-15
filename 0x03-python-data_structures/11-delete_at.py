#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    nwlist = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    lenght = len(my_list)
    for i in range(lenght):
        if i == idx:
            my_list.remove(my_list[idx])
    return my_list
