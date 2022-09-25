import string
from unittest import result
def weightUniformsStrings(s,queries):
    d = {ele: i for i , ele in enumerate(string.ascii_lowercase,start=1)}
    count = 1
    weight = set()
    for i , ele in enumerate(s):
        if i + 1 != len(s) and ele == s[i + 1]:
            count += 1
        else:
            count = 1
        weight.add(d[ele]*count)
    return ["Yes" if i in weight else "No" for i in queries]
        
        
 



s = input('s: ')
q = [1,3,12,5,9,10]
print(weightUniformsStrings(s,q))