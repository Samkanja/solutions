# def findMedian(arr):
#     arr.sort()
#     l = 0
#     r = len(arr) 
#     for i in range(len(arr)):
#         r = r - 1
#         if r == l:
#             return arr[i]
#         l = len(arr[:i+1])


# n = [0,1,2,4,6,5,3]
# print(findMedian(n))
# n = 9
# print(f'{n:032b}')
# print(int('10001',3))

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
new = [sorted([arr[j][i] for i in range(len(arr))], reverse=True) for j in range(len(arr))]
print(new)
las = [ ele for ele in arr]
print(las)
n = len(arr) - 1
diag = [arr[i][i] for i in range(len(arr))]
print(diag)
diaga = [arr[i][n- i] for i in range(len(arr))]
print(diaga)
v = 'We promptly judged antique ivory buckles for the prize'
v = ''.join(v.split())
print(v)
arr = [1,4,9,19]
arr.sort(reverse=True)
print(arr)
def func(default=[]):
    default.append('pthon')
    return default
print(func())
print(func())
print(func())