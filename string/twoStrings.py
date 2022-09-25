from typing import *

def twoString(s1:str,s2:str):
    for i in s1:
        if i in s2:
            return "YES"
    return "No"
s1 = input('string1: ')
s2 = input('string2: ')
print(twoString(s1,s2))