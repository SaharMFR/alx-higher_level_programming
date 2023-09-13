#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = ""
        max_score = 0
        for key, value in a_dictionary.items():
            if value > max_score:
                best = key
        return best
    return None
