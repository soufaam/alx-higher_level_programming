#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    moy = 0
    for item in my_list:
        sum += item[0] * item[1]
        moy += item[1]
    return sum / moy
