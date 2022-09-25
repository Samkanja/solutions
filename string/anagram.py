def anagram(s):
    d = {}
    l,r=0,len(s)-1
    while l <= r:
        # d1.append(s[l])
        d[s[r]] = 1 + d.get(s[r],0)
        r -= 1    
        l += 1
    # return d
    count = 0
    for i in range(len(s)//2):
        char = s[i]
        if char not in d:
            count += 1
        # d[s[i]] = 1 + d.get(s[i],0)

    return count

     

s = input('string: ')
print(anagram(s))