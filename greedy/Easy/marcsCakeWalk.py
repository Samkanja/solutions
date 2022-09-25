def marcsCakeWalk(calories):
    result = 0
    for i, cal in enumerate(sorted(calories, reverse=True)):
        result += ((2**i) * cal)

    return result



calorie = list(map(int, input('calorie: ').rstrip().split()))
print(marcsCakeWalk(calorie))