def isEven(n:int) -> None:
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

a, b, c = map(int, input().split())

isEven(a)
isEven(b)
isEven(c)
