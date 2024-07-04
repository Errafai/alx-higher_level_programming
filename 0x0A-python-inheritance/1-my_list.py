#!/usr/bin/pythoni3
"""this module contains the """


class MyList(list):
    """Mylist is a subclass of the list class"""

    def print_sorted(self):
        """print the sorted list in asending order"""
        l = self.copy()
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if (l[i] > l[j]):
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
        print(l)
