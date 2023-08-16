#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    if len(set_1) == 0 and len(set_2):
        return set_2
    elif len(set_2) == 0 and len(set_1):
        return set_1
    for element1 in set_1:
        for element2 in set_2:
            if element1 not in set_2:
                new_set.add(element1)
            if element2 not in set_1:
                new_set.add(element2)
    return new_set
