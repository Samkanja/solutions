from base64 import encode
import string
def ceaserCipher(s, k):
    d = {}
    alp = string.ascii_lowercase
    for i , ele in enumerate(alp):
        d[ele] = alp[(i + k) % 26]


    ecoded = ''
    for j in s:
        if j.isalpha():
            if j.isupper():
                ecoded += d[j].upper()
            else:
                ecoded += d[j]
            

        else:
            ecoded += j
    return ecoded
    # return d
  
   
        

    



s = input('messege: ')
k = int(input('key: '))
print(ceaserCipher(s, k))