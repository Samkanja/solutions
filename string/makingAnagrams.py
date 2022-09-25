from typing import *
def makingAnagrams(s1:str, s2:str) -> int:
    # count:int = 0
    return sum([abs(s1.count(l) - s2.count(l)) for l in set(s1 + s2)])
    

    # return count
s1 = input('string1: ')
s2 = input('string2: ')
print(makingAnagrams(s1, s2))

