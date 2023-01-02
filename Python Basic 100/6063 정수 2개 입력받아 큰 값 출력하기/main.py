a, b = map(int, input().split())

print((lambda x, y: x if x > y else y)(a, b))
