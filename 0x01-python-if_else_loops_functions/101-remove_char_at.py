#!/usr/bin/python3

def remove_char_at(str, n):
    idx = 0
    new_list = []
    new_str = ""
    if n > len(str):
        return str
    for index in range(len(str)):
        flag = False
        if index == n:
            if (idx + 1) < len(str):
                new_list.append(str[idx + 1])
                flag = True
        else:
            if idx < len(str):
                new_list.append(str[idx])
        if flag:
            idx += 1
        idx += 1
    for item in new_list:
        new_str += item
    return new_str
