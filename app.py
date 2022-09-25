# import sys

# def do_cat(name):
#     print(f"Meow, i'm {name}")

# def do_dog(name, kind="dog"):
#     print(f"Woof from {name}, a {kind}")
# print(sys.argv[1])
# if __name__ == '__main__':
#     cmd = sys.argv[1]
#     handler = globals()[f'do_{cmd}']
#     handler(*sys.argv[2:])
# print(5%5)
from typing import Counter


p = 1
q = 100
c = 0
# for i in range(p, q +1):
#     sqr = str(i**2)
#     n = len(sqr)
#     # print(sqr)
#     d = len(str(i))
#     r = int(sqr[n-d:])
#     try:
#         l = int(sqr[:n-d])
#     except:
#         l = 0

#     if (l + r == i):
#         print(i, end=' ')
#         c += 1
# if c == 0 : print('Ivalid range')



# b = ['kanja','sam']
# for j in range(len(b)):
#     print(b[j])
# y = [9,0,3,4]
# for x in range(len(y)):
#     print(y[x])
# a = [3, 5]
# l = []
# for i in range(0, len(a),2):
#     print(a[i])
#     if i + 1 < len(a):
#         print(a[i])
#         l.append(a[i+1]-a[i])
# print(abs(-2-2))
# arr = list(map(int,input('arr: ').rstrip().split()))
# print(sorted(arr))
        
grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
grid = [''.join(sorted(ele)) for i , ele in enumerate(grid)]
print(grid)
print([''.join(grid[j][i] for j in range(len(grid))) for i in range(len(grid))])
# print(*grid)
# print(' '.join(grid))
# print(' '.join(map(str, grid)))
# # def add(**kwargs):
# #     return sum(kwargs)

# # print(add(8,9,10,5,10))
# # print(int('1010',2))
# # n = 5
# # print('{:032b}'.format(n))
# # print(f'{n:032b}')
# n = 100
# print(n%7<2)
s = [[1,5,7],[8,0,9],[6,4,2]]
s = sum(s,[])
print(s)
import sys
def camel_case(q):
    return_str = ''
    # for i in q:       
    operator, detail, string = q.split(';')
    if operator =='C':
        new_str = ''
        for j in string.split(' '):
            new_str = new_str + j.capitalize()
        if detail =='M':
            new_str = new_str[0].lower() + new_str[1:]
            new_str = new_str + '()'
        elif detail == 'V':
            new_str = new_str[0].lower() + new_str[1:]
                
    elif operator == 'S':
        new_str = ''
        for i in (string[0].lower() + string[1:]).replace('()', ''): 
            if(i.isupper()):
                new_str += ' '+i.lower()
            else:
                new_str += i  

    return (new_str)
data = input('data: ')
# inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]
print(camel_case(data))

 

