from typing import *
def alternatingCharacters(s):
    l, r = 0, len(s) -1
    while l <= r:
        if s[l] != s[r]:
            if s[l + 1] == s[r]:
                return l
            elif s[l] == s[r + 1]:
                return r
            l += 1
            r -= 1
    return -1


q = input()
print(alternatingCharacters(q))