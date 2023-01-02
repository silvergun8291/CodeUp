w, h, b = map(int, input().split())

result = (((w * h * b) / 8) / 1024) / 1024

print(f'{result:.2f} MB')

