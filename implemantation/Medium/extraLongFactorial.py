def extraLongFactorial(n):
    if n == 1:
        return 1
    return n * extraLongFactorial(n - 1)

n = int(input('num: '))
print(extraLongFactorial(n))