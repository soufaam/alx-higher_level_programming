#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    if len(sys.argv) == 1:
        print("{}".format(sum))
    else:
        for iter in range(1, len(sys.argv)):
            sum += int(sys.argv[iter])
        print(sum)
