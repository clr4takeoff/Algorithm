#B1_1551_수열의 변화

n, k = map(int, input().split())
a = list(map(int, input().split(',')))

for _ in range(k):
    a = [a[i+1] - a[i] for i in range(len(a) - 1)]

print(','.join(map(str, a)))
