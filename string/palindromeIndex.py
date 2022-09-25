import re


def palindromeIndex(s):
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            if s[l + 1] == s[r]:
                return l
            elif s[l] == s[r - 1]:
                return r
        r -= 1
        l += 1
    return -1



s = input()
print(palindromeIndex(s))