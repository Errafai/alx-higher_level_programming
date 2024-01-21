#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) or idx < 0:
        return my_list
    return [i for i in my_list if i != my_list[idx]]
