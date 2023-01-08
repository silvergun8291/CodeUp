table = []

for i in range(10):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    

y = 1
x = 1
flag = False

while y < 10:
    while x < 10:   # 오른쪽으로 이동
        
        if (table[y][x] == 2) or (y == 8 and x == 8):    # 먹이를 찾으면 or 맨 아래 오른쪽에 도착하면
            table[y][x] = 9     # 9로 표시
            flag = True         # 이중 루프 탈출
            break
        

        if (table[y][x] == 1) and (table[y+1][x-1] == 1):  # 이동이 불가능하면
            flag = True     # 이중 루프 탈출
            break
        
        if (table[y][x] == 1) and (table[y+1][x-1] != 1):  # 오른쪽으로 이동이 불가능하면
            y = y + 1       # 아래로 이동
            x = x - 1
            continue
        
        table[y][x] = 9        # 방문 한 곳 9로 표시 
        
        x += 1
    
    if flag:    # 이중 루프 탈출
        break
    
    y += 1
    
    
for i in range(10):     # 결과 출력
    print(*table[i])