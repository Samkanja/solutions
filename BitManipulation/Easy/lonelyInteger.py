def lonely_integer(a):
    total =0
    for i in a:
        total ^= i
    return total


a = list(map(int, input('arr: ').rstrip().split()))
print(lonely_integer(a))