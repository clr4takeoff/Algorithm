#B4_5575_타임 카드

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return h, m, s

for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    start = to_seconds(h1, m1, s1)
    end = to_seconds(h2, m2, s2)
    work = end - start
    h, m, s = to_time(work)
    print(h, m, s)
