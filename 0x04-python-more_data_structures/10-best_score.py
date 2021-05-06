#!/usr/bin/python3


def best_score(a_dictionary):
    best = 0
    if a_dictionary == None:
        return None
    for x, y in a_dictionary.items():
        if y > best:
            best = y
            best_key = x
    return best_key
