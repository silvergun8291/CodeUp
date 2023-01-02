table = [[0 for x in range(19)] for y in range(19)]

size = int(input())

for i in range(size):
    x, y = map(int, input().split())
    table[x-1][y-1] = 1

for i in range(19):
    print(*table[i])
