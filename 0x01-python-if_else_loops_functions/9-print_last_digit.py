#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        result = number % 10
    else:
        result = number % -10
    if result < 0:
        result *= -1
    print(f'{result}', end='')
    return (result)
