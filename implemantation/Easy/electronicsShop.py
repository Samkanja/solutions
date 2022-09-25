def getMoneySpent(keyboards,drives,b):
    total = -1
    for i, ele in enumerate(keyboards):
        j = 0
        while j < len(drives):
            new = ele + drives[j]

            if new < b:
                total = max(new,total)
            
            # print(drives[j],ele)
            j += 1
        
            
            
    return total

b = 60
keyboards = [40,50,60]
drives = [5,8,12]
print(getMoneySpent(keyboards,drives,b))

