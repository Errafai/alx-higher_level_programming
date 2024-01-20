#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    m = dir(hidden_4)
    for i in m:
        if i[0] != "_":
            print("{}".format(i))
