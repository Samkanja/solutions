def flippingBits(n):
    b = bin(n)[2:]
    prefit = ''
    for i in range(32 -len(b)):
        prefit += '0'
    b = prefit + b
    flipped = ''
    for i in b:
        if i == '0':
            flipped += '1'
        else:
            flipped += '0'

    return int(flipped,2)


n = int(input('num: '))
print(flippingBits(n))  