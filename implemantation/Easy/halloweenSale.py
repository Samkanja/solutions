from itertools import count


def halloweenSale(p,d,m,s):
    count = 0
    budget =s
    while budget >= p:
        count += 1
        budget -= p
        p -= d
        if p <= m:
            p = m
      
    
        
    return count


first_multiple_input = input().rstrip().split()

p = int(first_multiple_input[0])

d = int(first_multiple_input[1])

m = int(first_multiple_input[2])

s = int(first_multiple_input[3])
print(halloweenSale(p,d,m,s))