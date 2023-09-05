#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i != j:
            print("{:d}".format(i), end='')
            if i != 8:
                print("{:d}".format(j), end=', ')
            else:
                print("{:d}".format(j))
