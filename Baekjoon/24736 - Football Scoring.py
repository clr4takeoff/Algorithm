#B5_24736_

v = list(map(int, input().split()))
h = list(map(int, input().split()))

def s(x):
    t, f, s, p, c = x
    return t * 6 + f * 3 + s * 2 + p + c * 2

print(s(v), s(h))
