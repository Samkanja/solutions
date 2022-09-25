def hackerrankString(s):
    t = 'hackerrank'
    count = 0
    for i in s:
        if i == t[count]:
            count += 1

        if count == len(t):
            return "YES"
    return "NO"

s = input('string: ')
print(hackerrankString(s))

    

      


    




print(hackerrankString(s))