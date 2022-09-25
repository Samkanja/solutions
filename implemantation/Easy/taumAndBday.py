from typing import *

def taumBday(b:int,w:int,bc:float,wc:float,z:float):
    return b *min(bc, wc+z) + w *min(wc, bc+z)
    # return min(((b+w)*bc + (w * z)), (((b + w)*wc) + (b * z)), (b * bc + w + wc))


b = int(input('b: '))
w = int(input('w: '))
bc = int(input('bc: '))
wc = int(input('wc: '))
z = int(input('w: '))

print(taumBday(b,w,bc,wc,z))