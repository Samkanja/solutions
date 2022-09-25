def gridChallenge(grid):
    grid = [''.join(sorted(ele)) for i , ele in enumerate(grid)]
    print(grid)
    print()
    new = [''.join(grid[j][i] for j in range(len(grid))) for i in range(len(grid[0]))]
    print(new)
    print()
    final = [''.join(sorted(row)) for row in new]
    print(final)
    print()
    if final == new:
        return "YES"

    return "NO"




t = int(input('num: '))
grid = []
for _ in range(t):
    grid_item = input('items: ')
    grid.append(grid_item)

print(gridChallenge(grid))
