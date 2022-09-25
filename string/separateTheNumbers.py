def separateNumbers(s):
    for i in range(1,1+len(s)//2):
        temp_num = int(s[:i])
        j = 0
        temp_str = ''
        while len(temp_str) < len(s):
            temp_str += str(temp_num + j)
            j += 1

        if temp_str == s:
            return f'Yes {temp_num}'
    return "No"


s = input()
print(separateNumbers(s))