#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    else:
        print("{}: arguments".format(len(sys.argv)))
        for iter in range(1, len(sys.argv)):
            print("{}: {}".format(iter, sys.argv[iter]))
