#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv) - 1
    if ln == 0:
        print("0 arguments.")
    elif ln == 1:
        print("1 arguments:")
    else:
        print(ln,"argument:")
    for i in range(ln):
        print(i + 1,":", sys.argv[i + 1])
