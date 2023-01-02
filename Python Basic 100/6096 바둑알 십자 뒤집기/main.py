table = []

for i in range(19):
    rows = list(map(int, input().split()))
    table.append(rows)


size = int(input())

for i in range(size):
    x, y = list(map(int, input().split()))

    for i in range(19):
        table[x-1][i] = int(not table[x-1][i])

    for i in range(19):
        table[i][y-1] = int(not table[i][y-1])

for i in range(19):
    print(*table[i])

