def jimOrder(orders):
    # count = 0
    # l = []
    # l = [(i , ele[1]+ele[0]) for i, ele in enumerate(orders,start=1)]
    #     # x, y = ele
    #     # total = x + y
    #     # l.append((total,i))
    # l.sort(key=lambda x:x[1])
    
    # return ' '.join(list(map(str,[i[0] for i in l])))

    return tuple(zip(*sorted(enumerate(map(sum,orders),1),key=lambda x:x[1])))
    # return (i[0] for i in s)

    # d = dict()
    # for i , ele in enumerate(orders,start=1):
    #     if sum(ele) not in d:
    #         d[sum(ele)] = [i]
    #     else:
    #         d[sum(ele)].append(i)
    # res = []
    # for key, value in sorted(d.items()):
    #     res.extend(value)

    # return res





# n = int(input('num: '))
# orders = []
# for i in range(n):
#     orders.append(list(map(int, input('List: ').rstrip().split())))
orders = [[8,1],[4,2],[5,6],[3,1],[4,3]]
orders = [[8,3],[5,6],[6,2],[2,3],[4,3]]

print(jimOrder(orders))
