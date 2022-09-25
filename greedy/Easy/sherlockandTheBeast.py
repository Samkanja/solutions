

def decentNumber(n):
    fives = n
    while fives % 3 !=0:
        fives -= 5
    return -1 if fives < 0 else '5' * fives + '3' *(n - fives)



n = int(input('num: '))
print(decentNumber(n))