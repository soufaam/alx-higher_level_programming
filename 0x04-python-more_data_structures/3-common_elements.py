#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                new_set.add(element1)
    return new_set
