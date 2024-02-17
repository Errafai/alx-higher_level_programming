#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
    except Exception:
        i -= 1
        print()
        pass
    finally:
        return i + 1
