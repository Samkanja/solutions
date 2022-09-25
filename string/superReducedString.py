def superReducedString(s):
    for i in s:
        if i*2 in s:
            s = s.replace(i*2,'')

   


    return 'Emtpy string' if len(s) == 0 else s







s = input()
print(superReducedString(s))