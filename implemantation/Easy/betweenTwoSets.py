def getTotalX(a, b):
    count = 0
    
    for num in range(a[-1],b[0]+1):
        if all(num % x==0 for x in a) and all(x % num == 0 for x in b):
            count += 1

    print(count)

    



arr1 = list(map(int, input('arr1: ').rstrip().split()))
arr2 = list(map(int, input('arr2: ').rstrip().split()))
print(getTotalX(arr1,arr2))