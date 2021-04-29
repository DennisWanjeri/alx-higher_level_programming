#!/usr/bin/python3

import sys

if __name__ == "__main__":
    i = 1
    length = len(sys.argv) - 1

    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments:".format(length))
    while i <= length:
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
