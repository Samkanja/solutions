from typing import *

def closestNumbers(arr):
    # d = {}
    # for i, ele in enumerate(arr):
    #     j = i + 1
    #     while j < len(arr):
    #         diff = abs(ele-arr[j])
    #         if diff not in d:
    #             d[diff] = []

    #         d[diff].extend([ele , arr[j]])
    #         j += 1
    # return d, min(d.items(), key=lambda x:x[0])[1]
    arr.sort()
    pairs = {}
    for i in range(len(arr)-1):
        diff = abs(arr[i]-arr[i +1])
        if diff not in pairs:
            pairs[diff] = []
        pairs[diff].extend([arr[i],arr[i +1]])
    return pairs[min(pairs.keys())]

    

arr = list(map(int,input('arr: ').rstrip().split()))
print(closestNumbers(arr))