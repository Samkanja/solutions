def kangaroo(x1, v1,x2,v2):
    if x1 < x2 and v1 < v2:
        return "NO"
    else:
        if v1 != v2 and (x2 - x1) % (v2 - v1) == 0:
            return "YES"
        else:
            return "NO"
   

first = input('>: ').rstrip().split()
x1 = int(first[0])
v1 = int(first[1])
x2 = int(first[2])
v2 = int(first[3])
print(kangaroo(x1,v1,x2,v2))