#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    best_score = 0
    for key in a_dictionary.keys():
        if best_score < a_dictionary[key]:
            best_score = a_dictionary[key]
    return best_score
