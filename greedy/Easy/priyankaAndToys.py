def toys(w):
    count = 1
    w.sort()
    small = w[0]
    for a in w:
        if a > small + 4:
            small = a 
            count += 1
    return count

    


w = list(map(int, input('items: ').rstrip().split()))
print(toys(w))