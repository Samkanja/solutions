from typing import *
from collections.abc import Iterable, Sequence
def workbook(n: int, k:int, arr:Sequence[int]):
    pages = 1
    count = 0
    chapters = 0
    for ar in arr:
        for i in range(1, ar+1):
            if i == pages:
                count += 1

            if i == ar or i  % k == 0:
                pages += 1

    return count

n:int = int(input('num: '))
k: int= int(input('problems: '))
arr: Sequence[int] = list(map(int,input('chapters: ').rstrip().split()))
print(workbook(n,k,arr))