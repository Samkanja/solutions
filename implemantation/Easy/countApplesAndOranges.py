def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here0
    countA = 0
    for apple in apples:
        # d = a + apple
        if (a+apple) in range(s,t+1):
            countA += 1
    print(countA)
    countB = 0
    for orange in oranges:
        #d = b + orange
        if (b+orange) in range(s,t+1):
            countB += 1
    print(countB)
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))[:m]

    oranges = list(map(int, input().rstrip().split()))[:n]

    countApplesAndOranges(s, t, a, b, apples, oranges)
