def queensAttack(n, k r_q,c_q,obstacles):
    ...

first_multiple = input('num: ').rstrip().split()
n = int(first_multiple[0])
k = int(first_multiple[1])
second_multiple = input('num2: ').rstrip().split()
r_q = int(second_multiple[0])
c_q = int(second_multiple[1])
obstacles = []
for _ in range(k):
    obstacles.append(list(map(int, input().rstrip().split())))

print(queensAttack(n, k, r_q,c_q,obstacles))
