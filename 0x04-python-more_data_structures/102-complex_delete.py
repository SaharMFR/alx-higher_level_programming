#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    if a_dictionary:
        for key, d_value in a_dictionary.items():
            if d_value == value:
                keys.append(key)

        for key in keys:
            del a_dictionary[key]

    return a_dictionary
