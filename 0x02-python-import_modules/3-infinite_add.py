#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    sum = 0
    length = len(sys.argv) - 1
    while i <= length:
        sum += int(sys.argv[i])
        i += 1
    print("{}".format(sum))
