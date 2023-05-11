#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    objects = dir(hidden_4)
    for i in objects:
        if i[0] != "_":
            print("{}".format(i))
