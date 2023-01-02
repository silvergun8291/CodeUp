n = int(input())
list = [x for x in range(1, n+1) if x % 3 != 0]

for i in list:
    print(i, end=" ")

