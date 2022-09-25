def countingValleys(steps,path):
    level = count = 0
    for ele in path:
        if ele == 'U':
            level += 1
        else:
            level -= 1
        if level == 0 and ele == 'U':
            count += 1

    return count

        


steps = int(input('steps: '))
path = input('path: ')[:steps]
print(countingValleys(steps,path))