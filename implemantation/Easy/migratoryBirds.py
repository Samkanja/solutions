def migratoryBirds(arr):
    d = {}
    for i , ar in enumerate(set(arr)):
        d[ar] = arr.count(ar)

    return max(d,key=(lambda x:d[x]))


# arr = list(map(int, input(">: ").rstrip().split()))
arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))