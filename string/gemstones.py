def gemstones(s):
    return len(set(s[0]).intersection(*set(j for j in s[::])))

    

        

arr = []
n = int(input('num: '))
for _ in range(n):
    arrItem = input('string: ')
    arr.append(arrItem)

print(gemstones(arr))