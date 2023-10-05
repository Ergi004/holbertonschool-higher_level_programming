#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string != str(roman_string) or roman_string is None:
        return 0
    romanNum = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'W': 1000
            }
    value = 0
    for i in range(len(roman_string) - 1):
        if romanNum[roman_string[i]] < romanNum[roman_string[i + 1]]:
            value -= romanNum[roman_string[i]]
        else:
            value += romanNum[roman_string[i]]
    value += romanNum[roman_string[-1]]
    return value
