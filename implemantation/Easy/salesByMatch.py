def sockMerchant(n, ar):
    d = {}
    count = 0
    for i , ele in enumerate(ar):
        d[ele] = 1 + d.get(ele,0)
        if d[ele] % 2 == 0:
            count += 1

    return count

n = int(input('arr: ').strip())
arr = list(map(int,input('>: ').rstrip().split()))[:n]
print(sockMerchant(n,arr))