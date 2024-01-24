#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max = list(a_dictionary.item())[0][0]
    for i, j in a_dictionary.items():
        if a_dictionary[i] >= a_dictionary[max]:
            max = i
    return max
