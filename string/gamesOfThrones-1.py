def gameOfThrones(s: str) -> str:
    d = {}
    for i in s:
        d[i] = 1 +d.get(s,0)
    count = 0
    for key, value in d.items():
        if value % 2 == 0:
            count += 1

        if count > 1:
            return "NO"
    return "YES"


s = input()
print(gameOfThrones(s))