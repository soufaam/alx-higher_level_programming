#!/usr/bin/python
import hidden_4 as hi

if __name__ == "__main__":
    plt = dir(hi)
    for item in plt:
        if not item.startswith("_"):
            print(item)
