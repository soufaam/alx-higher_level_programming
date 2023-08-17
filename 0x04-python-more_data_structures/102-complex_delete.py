#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lt = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            lt.append(key)
    for element in lt:
        a_dictionary.pop(element)
    return a_dictionary
