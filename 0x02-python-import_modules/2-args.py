#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    nArgs = len(sys.argv) - 1

    if nArgs == 0:
        print("0 arguments.")
    elif nArgs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nArgs))

    for i in range(1, nArgs + 1):
        print("{}: {}".format(i, sys.argv[i]))
