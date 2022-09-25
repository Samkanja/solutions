def fairRations(B):
    count = 0
    for i, ele in enumerate(B):
        if ele % 2 == 1:
            if i + 1 < len(B):
                ele += 1
                B[i + 1] += 1
                count += 2
            else:
                return "NO"
    return count

B = list(map(int, input('List:').rstrip().split()))
print(fairRations(B))