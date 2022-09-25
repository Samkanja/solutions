def climbingLeaderboard(ranked, player):
    # ranked =list(set(ranked))
    # ranked.sort()
    # n = len(ranked)
    # res = []
    # i = 0
    # for score in player:
    #     while i < n and ranked[i] <= score:
    #         i += 1
    #     res.append(n - i + 1)
    # return res
    # for i in range(len(ranked)):
    # a  = player[0]
    # ranked_new = ranked.insert(0, a)
    # print(ranked_new)
    res = []
    number = 1
    ranked = list(dict.fromkeys(ranked, number))
    for score in player:
        while len(ranked) > 0 and score >= ranked[-1]:
            ranked.pop()
        res.append(len(ranked) + 1)
        ranked.append(score)
    return res
        





ranked = list(map(int, input('ranked: ').rstrip().split()))
player = list(map(int, input('player: ').rstrip().split()))
print(climbingLeaderboard(ranked, player))