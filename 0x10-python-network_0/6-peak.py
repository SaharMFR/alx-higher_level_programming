#!/usr/bin/python3
""" The function `find_peak` finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Takes a list of integers and finds the peak of it, then returns the peak.
    """

    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2

    if list_of_integers[mid] >= list_of_integers[mid + 1] and\
            list_of_integers[mid] >= list_of_integers[mid - 1]:
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
