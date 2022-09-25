def birthday(s,d,m):
    count = 0
    for i, ele in enumerate(s):
        if sum(s[i:i+m]) == d:
            count += 1

    return count
    
    





# s = list(map(int,input('>: ').rstrip().split()))
s = [4]
d = int(input('day: '))
m = int(input('month: '))
print(birthday(s,d,m))