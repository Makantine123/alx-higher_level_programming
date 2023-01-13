#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArg = len(sys.argv)
    sumArgv = 0
    if (numArg > 1):
        for i in range(numArg):
            if i == 0:
                continue
            argvValue = int(sys.argv[i])
            sumArgv = sumArgv + argvValue
    print("{:d}".format(sumArgv))
