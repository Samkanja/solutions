from typing import *
# d = {(6,7):4,(9,0):9}
# print(d)
# l = [(9,6),(10,7),(4,5)]
# p = []
# for x, y in l:
#     p.append(x)
#     p.append(y)

# print(p)
# p = sum(l,())
# print(p)
a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

# for i in range(len(a)):
#     # print(a[i])
#     for j in range(len(a)):
#         # print(a[j])
#         # print(a[i][j])
#         print(a[j][i])

# a = ['ebcad','fghij','olmkn','trpqs','xywuv']
# new = [''.join(sorted(row)) for row in a]
# p = [''.join([new[j][i] for i in range(len(new))]) for j in range(len(new))]
# print(p)
# r = [''.join(sorted(row)) for row in p]
# print(r)
k = 4
arr =[1,2,3,4,10,20,30,40,100,200]
for i in range(len(arr)-k+1):
    print(arr[i+k-1] -  arr[i])
