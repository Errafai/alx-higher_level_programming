#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            pass
        except IndexError as II:
            raise (II)
    print()
    return n
