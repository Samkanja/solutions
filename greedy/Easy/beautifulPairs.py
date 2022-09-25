def beautifulPairs(A,B):
    da = {}
    db = {}
    for a in A:
        da[a] = 1 + da.get(a, 0)
    for b in B:
        db[b] = 1 + db.get(b,0)
    be_set = 0
    for val in da:
        if val in db:
            be_set += min(db[val], da[val])
    return be_set - 1 if be_set == len(A) else be_set + 1
        

A = list(map(int, input('list1: ').rstrip().split()))
B = list(map(int,input('list2: ').rstrip().split()))
print(beautifulPairs(A,B))