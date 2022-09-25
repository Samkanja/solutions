


def beautifulTriplets(d, arr):
    count = 0
    for i , ele in enumerate(arr):
        if ele + d in arr and ele + 2*d in arr:
            count+=1
    return count




n = int(input('num: '))
arr = list(map(int, input('list: ').rstrip().split()))
print(beautifulTriplets(n,arr))