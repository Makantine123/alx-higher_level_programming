#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    numArg = len(sys.argv)

    if numArg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        oper = sys.argv[2]
        a = sys.argv[1]
        b = sys.argv[3]

        if oper not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(a)
            b = int(b)

            if oper == "+":
                result = add(a, b)
            elif oper == "-":
                result = sub(a, b)
            elif oper == "*":
                result = mul(a, b)
            elif oper == "/":
                result = div(a, b)

            print("{:d} {:s} {:d} = {:d}".format(a, oper, b, result))
