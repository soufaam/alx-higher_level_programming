#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_score = 0
    for key in a_dictionary.keys():
        if best_score < a_dictionary[key]:
            best_score = a_dictionary[key]
    return best_score
