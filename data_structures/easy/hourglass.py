from typing import *
def hour_glass(arr:List[List[float]]) -> float:
    total = 0
    for row in range(len(arr)-2):
        for col in range(len(arr)-2):
            top = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            mid = arr[row+1][col+1]
            bottom = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            total = max(top+bottom+mid,total)

    return total

arr = []
for _ in range(6):
    arr.append(list(map(int,input('arr: ').rstrip().split())))

print(hour_glass(arr))