#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == 8 and j == 9:
            print("89")
            break
        else:
            if i != j and j > i:
                 print("{}{}, ".format(i, j),end = "")
