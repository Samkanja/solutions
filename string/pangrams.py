import string
def pangrams(s):
    d = {}
    for i in string.ascii_lowercase:
        d[i] = 1 + d.get(i,0)
    for ele in s.lower():
        d[ele] = 1 + d.get(ele,0)

    print(d)
    for i , v in d.items():
        if d[i] < 2:
            return 'NOT pangram'
    return "pangram"




s = input()
print(pangrams(s))