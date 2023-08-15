#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    nwlist = []
    if idx < 0 or idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            my_list.remove(my_list[idx])
            continue
        else:
            nwlist.append(my_list[i])
    my_list = nwlist
    return my_list
