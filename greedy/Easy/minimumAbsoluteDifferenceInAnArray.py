def minimumAbsoluteDifference(arr):
    minm = float('inf')
    arr = sorted(arr)
    print(arr)
    for i  in range(len(arr)-1):
        # print(abs(arr[i] - arr[i + 1]))
        minm = min(abs(arr[i+1]-arr[i]), minm)
       
    return minm

arr = list(map(int,input('arr: ').rstrip().split()))
print(minimumAbsoluteDifference(arr))
