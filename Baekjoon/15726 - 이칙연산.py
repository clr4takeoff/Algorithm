#B4_15726_이칙연산

a, b, c = map(int, input().split())
x = (a * b) / c
y = (a / b) * c
if x > y:
    print(int(x))
else:
    print(int(y))