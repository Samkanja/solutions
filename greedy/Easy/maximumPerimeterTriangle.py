def maximumPerimeterTriangle(sticks):
    maxPeri = 0
    key = None
    sticks.sort()
    for i in range(len(sticks)-2):
        l = []
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            # l.extend([sticks[i],sticks[i +1],sticks[i +2]])
            maxPeri = max(maxPeri, sum(sticks[i:i+3]))
            key = i
    return -1 if key == None else sticks[key:key+3]

sticks = list(map(int,input('list: ').rstrip().split()))
print(maximumPerimeterTriangle(sticks))