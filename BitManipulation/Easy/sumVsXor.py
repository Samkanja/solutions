def sumXor(n):
    # count = 0
    # for i in range(n+1):
    #     if n + i == n ^ i:
    #         count += 1

    # return count
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n >>=1
    return 1 << count

n = int(input('num: '))
print(sumXor(n))
