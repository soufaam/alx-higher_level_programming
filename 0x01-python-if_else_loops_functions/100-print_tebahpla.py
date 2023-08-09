#!/usr/bin/python3


for number in range(122, 96, -1):
    if number % 2 == 0:
        print(chr(number), end='')
    else:
        print(chr(number-32), end='')
