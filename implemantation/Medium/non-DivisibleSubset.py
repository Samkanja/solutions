def nonDivisibleSubset(s, k):
    count = 0
    l = []
    for i, ele in enumerate(s):
        j = i + 1
        while j < len(s):
            if (s[j] + ele)%k != 0:
                count += 1
                l.extend([s[j],ele])

            j += 1

    return len(set(l))

s = list(map(int, input('list: ').rstrip().split()))
k = int(input('num: '))
print(nonDivisibleSubset(s, k))