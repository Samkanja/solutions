from typing import *

def kaprekarNumbers(p:int,q:int) -> int:
    last = []
    for i in range(p, q):
        d = len(str(i))
        new = i**2
        digit = []
        total = []
        while new > 0:
            digit.append(new%10)
            new = int(new//10)
        print(digit,i,d)
        for j in range(0,len(digit[::-1]),d):
            total+=(digit[i:d])
        if total == i:
            last.append(i)
        print(total)



    return last





p = int(input('int1: '))
q = int(input('int2: '))
print(kaprekarNumbers(p,q))