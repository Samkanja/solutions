def chocolateFeast(n,c,m):
    count = n // c
    choco = count
    while  choco >= m:
        a,b= divmod(choco,m)
        count += a
        choco = a + b
    return count
 
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
c = int(first_multiple_input[1])

m = int(first_multiple_input[2])

# s = int(first_multiple_input[3])
print(chocolateFeast(n,c,m))