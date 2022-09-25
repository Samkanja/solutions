def bonAppetit(bill,k,b):

    return 'Bon Appetit'  if ((sum(bill)-bill[k])/2) == b else int(b - ((sum(bill)-bill[k])/2))




bill = list(map(int,input('>: ').rstrip().split()))
k = int(input('item: '))
b = int(input('cash: '))
print(bonAppetit(bill,k,b))