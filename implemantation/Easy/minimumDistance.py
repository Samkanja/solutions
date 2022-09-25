




def minimumDistance(a):
    s = set(i for i in a if a.count(i) == 2)
    dif = set(abs(a.index(i) - a.index(i,a.index(i)+1)) for i in s)
    return min(dif)

   


a = list(map(int, input('list: ').rstrip().split()))
print(minimumDistance(a))