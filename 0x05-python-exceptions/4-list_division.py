#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    d = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            div = 0
            print("out of range")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        finally:
            d.append(div)
    return d
