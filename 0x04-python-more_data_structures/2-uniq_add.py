#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique = []

    for i in my_list:
        if i not in unique:
            unique.append(i)
            result += i

    return result
