#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguements.")
    elif length == 1:
        print("{:d} arguement:".format(length))
    else:
        print("{:d} arguements:".format(length))
    while i <= length:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
