def pickingNumbers(a):
    

       


    return max([a.count(i)+ a.count(i -1) for i in a])



a = list(map(int,input(">: ").rstrip().split()))
print(pickingNumbers(a))