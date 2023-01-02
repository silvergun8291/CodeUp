h, b, c, s = map(int, input().split())

result = (((h * b * c * s) / 8) / 1024) / 1024
print(f'{result:.1f} MB')
