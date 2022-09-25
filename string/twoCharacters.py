def alternate(s):
    slist = list(set(s))
    print(slist)
    count = 0
    for i , ele in enumerate(slist):
        # c = i + 1
        for c in range(i + 1, len(slist) ):
            print(ele, slist[c])
            # c += 1
            case = [z for z in s if z == ele or z == slist[c]]
            print(case)
            if len(set(case[::2])) == 1 and len(set(case[1::2])) == 1:
                count = max(len(case),count)
    return count


s = 'beabeefeab'
print(alternate(s))