#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArg = len(sys.argv) - 1
    if (numArg == 1):
        print("{:d} argument:".format(numArg))
    else:
        print("{:d} arguments:".format(numArg))
        i = 1
        for i in range(numArg):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
