#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for i, j in a_dictionary.items():
        if j > maxval:
            maxkey = i
            maxval = j
    return maxkey
