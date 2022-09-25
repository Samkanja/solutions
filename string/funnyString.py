def funnyString(s):
    # def change(x,y):
    #     if x > y:
    #         x,y = y,x
    #     else:
    #         y,x=x,y
    last = [ord(ele) for i , ele in enumerate(s)]
    l =[abs(ord(s[i]) -ord(s[i-1])) for i in range(1,len(s))]
    return 'Funny' if l == l[::-1] else 'Not Funny'
s = input()
print(funnyString(s))