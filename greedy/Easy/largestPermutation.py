def largestPermutation(k, arr):
    # arr.sort()
    # new = arr
    # r = len(new)-1
    # l = 0
   
    # while l <= r:
    #     while k > 0:
    #         new[l],new[r] = new[r], new[l]
    #         k -= 1
    #     r -= 1
    #     l += 1

    # return new
    i = 0
    n = len(arr)
    while k > 0:
        # if i == n:
        #     return arr
        j = arr.index(max(arr[i:]))
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j] , arr[i]
            k -= 1
        i += 1
    return arr


arr = list(map(int, input('arr: ').rstrip().split()))
k = int(input('K: '))
print(largestPermutation(k,arr))