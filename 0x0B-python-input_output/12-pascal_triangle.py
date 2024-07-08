#!/usr/bin/python3
"""this module implement the function to construct the
pascale triangle"""


def pascal_triangle(n):
    """construct the pascale triangle using nested loops"""

    tr = []
    if n <= 0:
        return [[]]
    tr.append([1])
    if n == 0:
        return tr
    tr.append([1, 1])
    if n == 1:
        return tr
    for i in range(2, n):
        ll = []
        ll.append(1)
        for j in range(1, i):
            ll.append(tr[i - 1][j-1] + tr[i-1][j])
        ll.append(1)
        tr.append(ll)
    return tr
