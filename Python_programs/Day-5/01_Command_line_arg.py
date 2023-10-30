#Variables
import sys


def add(a,b):
    result1= a+b
    return result1

def mul(a,b):
    result2=a*b
    return result2

a=int(sys.argv[1])
operation=sys.argv[2]
b=int(sys.argv[3])


if operation=="add":
    output = add(a,b)
    print(output)