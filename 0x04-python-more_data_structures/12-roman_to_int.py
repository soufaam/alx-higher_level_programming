#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    roman = {"X": 10, "V": 5, "C": 100, "D": 500, "L": 50, "I": 1, "M": 1000}
    if "str" not in str(type(roman_string)) or roman_string is None:
        return 0
    for idx in range(len(roman_string)):
        if roman_string[idx] in roman.keys():
            sum += roman[roman_string[idx]]
        if roman_string[idx] == "V" or roman_string[idx] == "X":
            if idx > 0 and roman_string[idx - 1] == "I":
                sum -= 2
        if roman_string[idx] == "C":
            if idx > 0 and roman_string[idx - 1] == "X":
                sum -= 20
    return sum
