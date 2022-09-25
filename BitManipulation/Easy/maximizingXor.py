def maximizingXor(l,r):
    maxj = 0
    for i in range(l,r+1):
        for j in range(l, r+1):
            maxj = max(i^j,maxj)

    return maxj
            

print(maximizingXor(11,100))



