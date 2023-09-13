#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    my_num = 0
    if isinstance(roman_string, str) and roman_string:
        for i in range(0, len(roman_string) - 1):
            if roman_string[i] in roman_numbers:
                if roman_numbers[roman_string[i]] >= \
                        roman_numbers[roman_string[i + 1]]:
                    my_num += roman_numbers[roman_string[i]]
                else:
                    my_num -= roman_numbers[roman_string[i]]
        my_num += roman_numbers[roman_string[len(roman_string) - 1]]
    return my_num
