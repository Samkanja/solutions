def beautifulBinaryString(b):
    count , i =0,0
    while i < len(b):
        if b[i:i+3] == '010':
            count += 1
            i += 3
        else:
            i += 1
    
    return count
    




b = input()
print(beautifulBinaryString(b))

