def climbingLeaderboard(ranked,player):
    d = {}
    for i, ele in enumerate(sorted(ranked), start=1):
        if ele in d:
            d[ele]  = i + 1
        d[ele] = i

    return d


ranked = list(map(int,input('ranked: ').rstrip().split()))
player =  list(map(int,input('player: ').rstrip().split()))
print(climbingLeaderboard(ranked,player))