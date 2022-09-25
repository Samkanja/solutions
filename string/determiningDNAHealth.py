def determiningDnaHealth(l):
    total = maxtotal = mintotal = 0
    # dna = list(zip(genes,health))
    for i , ele in enumerate(l):
        print(ele)



    



# n = int(input('num: '))
# genes = input('genes: ').rstrip().split()[:n]
# health = list(map(int,input('health: ').rstrip().split()))[:n]
s = int(input('num_sstrands: '))
l = []
for _ in range(s):
    strands = input('stands: ').rstrip().split()
    j = []
    for i in range(len(strands)):
        first = int(strands[0])
        j.append(first)
        last = int(strands[1])
        j.append(last)
        d = strands[2]
        j = [first, last,d]
    l.append(j)
        
print(determiningDnaHealth(l))