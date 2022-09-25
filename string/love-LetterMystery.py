from typing import *
def theLoveLetterMystery(s:str) -> int:
    count = 0
    l = 0
    r = len(s)-1
    while l<=r:
        if s[l] != s[r]:
            count += abs(ord(s[l])-ord(s[r]))
        r -= 1
        l += 1
    return count
          
    

s:str = input()
print(theLoveLetterMystery(s))