n = int(input())

for i in range(1, n + 1):
    if str(i).find('3') != -1:
        print('X', end = ' ')
    elif str(i).find('6') != -1:
        print('X', end = ' ')
    elif str(i).find('9') != -1:
        print('X', end = ' ')
    else:
        print(i, end = ' ')

