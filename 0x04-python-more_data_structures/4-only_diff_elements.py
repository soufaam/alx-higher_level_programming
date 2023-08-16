#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for element1 in set_1:
        for element2 in set_2:
            if element1 != element2:
                new_set.add(element1)
                new_set.add(element2)
    return new_set
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
