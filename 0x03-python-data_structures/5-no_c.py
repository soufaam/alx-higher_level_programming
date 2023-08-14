#!/usr/bin/python3
def no_c(my_string):
    copy_list = []
    for idx in range(0, len(my_string)):
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            continue
        else:
            copy_list.append(my_string[idx])
    copy_string = ''
    for item in copy_list:
        copy_string += item
    return copy_string
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))