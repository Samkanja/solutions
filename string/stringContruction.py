from typing import *

def stringContruction(s:str) -> int:
    p: str = ''
    count = 0
    for i in s:
        if i in p:
            len(p)
        else:
            p += i
            count += 1
    return count
s: str = input('str: ')
print(stringContruction(s))
