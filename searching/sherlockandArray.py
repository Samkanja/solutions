def balanceSums(arr):
    suml = 0
    sumr = sum(arr)
    
    for i , ele in enumerate(arr):
        sumr -= ele
        if suml == sumr:
            
            return "YES"
        suml += ele
            
        
    return "NO"

arr = list(map(int, input('list: ').rstrip().split()))
print(balanceSums(arr))