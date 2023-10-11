#!/usr/bin/python3
"""Defines a script to read `stdin` line by line and computes metrics"""
import sys


def print_stats(size, st_codes):
    """Prints metrics"""
    print("File size: {}".format(size))
    for key in sorted(st_codes):
        print("{}: {}".format(key, st_codes[key]))


if __name__ == "__main__":

    size = 0
    st_codes = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, st_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if st_codes.get(line[-2], -1) == -1:
                        st_codes[line[-2]] = 1
                    else:
                        st_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, st_codes)

    except KeyboardInterrupt:
        print_stats(size, st_codes)
        raise
