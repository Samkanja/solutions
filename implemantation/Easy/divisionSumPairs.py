def divisibleSumPairs(k,arr):
    count = 0
    for i , ele in enumerate(arr):
        j = i +1
        while j < len(arr):
            print(arr[j],ele)
            if (arr[j] +ele) %  k == 0:
                count += 1
            # j += 1

    return count



k = int(input('>: '))
arr = list(map(int,input('list: ').rstrip().split()))
arr = [1,3,2,6,1,2]
print(divisibleSumPairs(k, arr))