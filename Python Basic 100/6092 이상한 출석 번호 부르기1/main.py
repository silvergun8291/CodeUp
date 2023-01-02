size = int(input())
num = list(map(int, input().split()))
result = [0 for x in range(23)]

for i in num:
    result[i-1] = result[i-1] + 1

print(*result)
