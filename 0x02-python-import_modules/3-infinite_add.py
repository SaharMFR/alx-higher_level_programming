#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0

    for i in range(1, len(sys.argv) + 1):
        result += int(argv[i])

    print(result)
