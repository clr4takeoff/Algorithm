#B4_6888_Terms of Office

import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def f(lst):
    t = lst[0]
    for n in lst[1:]:
        t = lcm(t, n)
    return t

def solve(x, y):
    p = f([4, 2, 3, 5])
    while x <= y:
        print(f"All positions change in year {x}")
        x += p

x = int(input())
y = int(input())
solve(x, y)
