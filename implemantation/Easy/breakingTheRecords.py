def  breakingRecords(scores):
    highest = scores[0]
    countH = 0
    lowest = scores[0]
    countL = 0
    for i, score in enumerate(scores):
        if score > highest:
            highest = score
            countH += 1
        if score < lowest:
            lowest = score
            countL += 1

    return countH,countL



scores = [10,5,20,20,4,5,2,25,1]
scores = list(map(int, input(">: ").rstrip().split()))
print(breakingRecords(scores))