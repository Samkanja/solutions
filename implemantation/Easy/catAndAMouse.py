def catAndMouse(x,y,z):
    if abs(z - x) > abs(z - y):
        return "CAT B"
    elif abs(z - y ) > abs(z - x):
        return 'CAT A'
    else:
        return 'MOUSE C'


xyx= input().split()
x = int(xyx[0])
y = int(xyx[1])
z = int(xyx[2])
print(catAndMouse( x,y,z))