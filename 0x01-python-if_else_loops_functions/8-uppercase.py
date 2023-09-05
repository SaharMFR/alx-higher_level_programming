#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if 97 <= ord(str[i]) <= 122:
            print("{:c}".format(ord(str[i]) - 32), end='')
        else:
            print("{}".format(str[i]), end='')
