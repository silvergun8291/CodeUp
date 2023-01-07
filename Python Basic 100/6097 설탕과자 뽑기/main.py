h, w = map(int, input().split())
n = int(input())
table = [[0 for i in range(w)] for j in range(h)]


for i in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:  # 가로이면
        for i in range(l):
            table[x-1][y+i-1] = 1
    elif d == 1: # 세로이면
        for i in range(l):
            table[x+i-1][y-1] = 1


# 결과 출력
for i in range(h):
    for j in range(w):
        print(table[i][j])

