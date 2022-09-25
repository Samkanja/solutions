from typing import *
from collections.abc import Sequence,Iterable
def serviceLane(n:Iterable[int],cases:Iterable[List]):
    less = []
    for new in cases:
        x, y = new

        print(x,y)

        
    


width:List[int] = list(map(int, input('widths: ').rstrip().split()))
case : Iterable[List] = []
t = int(input('nums: '))
for _ in range(t):
    case.append(list(map(int,input('cases: ').rstrip().split())))

print(serviceLane(width, case))