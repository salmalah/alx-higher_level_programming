#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    oper = sys.argv[2]
    b = int(sys.argv[3])
    add = calc.add(a, b)
    sub = calc.sub(a, b)
    mul = calc.mul(a, b)
    div = calc.div(a, b)
    if oper == '+':
        print("{} + {} = {}" .format(a, b, add))
    elif oper == '-':
        print("{} - {} = {}" .format(a, b, sub))
    elif oper == '*':
        print("{} * {} = {}" .format(a, b, mul))
    elif oper == '/':
        print("{} / {} = {}" .format(a, b, div))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
