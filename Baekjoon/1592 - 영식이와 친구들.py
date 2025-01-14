#B2_1592_영식이와 친구들

N, M, L = map(int, input().split())
c = [0] * N
i = 0
t = 0
while True:
    c[i] += 1
    if c[i] == M:
        break
    t += 1
    i = (i + L) % N if c[i] % 2 else (i - L) % N
print(t)
