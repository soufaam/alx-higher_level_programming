#!/usr/bin/python3
import sys
if __name__ == "__main__":
    import calculator_1 as cal
    a = int(sys.argv[1])
    opt = sys.argv[2]
    b = int(sys.argv[3])
    if opt == "+":
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif opt == "-":
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif opt == "*":
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif opt == "/":
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
