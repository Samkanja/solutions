def luckBalance(k, contests):
    total = count = 0
    for x, y in sorted(contests, reverse=True):
        if y == 1 and count < k:
            total += x
            count += 1
        elif y == 1 and count == k:
            total -= x
        else:
            total += x
    return total

   


k = int(input('k: '))
n = int(input('num: '))
contests = []
for _ in range(n):
    contests.append(list(map(int, input('list: ').rstrip().split())))
print(luckBalance(k, contests))
