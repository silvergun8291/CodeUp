table = []

for i in range(10):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    
    
table[1][1] = 9 # 시작 위치
    
for y in range(1, 10):
    for x in range(1, 10):
        if table[y][x] == 2:    # 먹이를 찾으면
            break
        elif (table[y][x+1] == 1) or (table[y+1][x] == 1):  # 이동이 불가능하면
            break
        elif table[9][x] == 1:  # 맨 아래 오른쪽에 도착하면
            break
        
        if table[y][x+1] != 1:  # 오른쪽으로 이동
            table[y][x+1] = 9
        elif table[y+1][x] != 1:  # 아래로 이동
            table[y+1][x] = 9
        
print()
for i in range(10):
    print(*table[i])