#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        n1 = int(sys.argv[1])
        operator = sys.argv[2]
        n2 = int(sys.argv[3])
        if operator == '+':
            print("{} + {} = {}".format(n1, n2, add(n1, n2)))
        elif operator == '-':
            print("{} - {} = {}".format(n1, n2, sub(n1, n2)))
        elif operator == '*':
            print("{} * {} = {}".format(n1, n2, mul(n1, n2)))
        elif operator == '/':
            print("{} / {} = {}".format(n1, n2, div(n1, n2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
