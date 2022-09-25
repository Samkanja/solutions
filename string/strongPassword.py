import string
def strongPassword(n,password):
    l = [0,0,0,0]
    for ele in password:
        if ele.isdigit():
            l[0] = 1
        elif ele.islower():
            l[1] = 1
        elif ele.isupper():
            l[2] = 1
        elif ele in string.punctuation:
            l[3] = 1
    return max(6 -len(password),4 -sum(l))
    
    




n = int(input('length: '))
password = input('password: ')
print(strongPassword(n,password))