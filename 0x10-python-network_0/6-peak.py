#!/usr/bin/python3
"""This module contains a function that finds the peak"""

def find_peak(list_of_integers):
    """find the peak using a loop and conditions"""
    
    list = list_of_integers

    if len(list) == 0:
        return None

    for i in range(1, len(list) - 1):
        if list[i] >= list[i - 1] and list[i] >= list[i + 1]:
            return list[i]
