n = int(input())
sum = 0

for i in range(0, n+1):
    sum = sum + i
    
    if sum >= n:
        print(i)
        break
        

