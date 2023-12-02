#!/usr/bin/python3
"""A function that finds a peak in a
list of unsorted integers."""
def find_peak(list_of_integers):
    """A function that finds a peak in a
    list of unsorted integers."""
    if list_of_integers == []:
        return None
    min = list_of_integers[0]
    for idx in range(len(list_of_integers)):
        if list_of_integers[idx] > min:
            min = list_of_integers[idx]
    return min
