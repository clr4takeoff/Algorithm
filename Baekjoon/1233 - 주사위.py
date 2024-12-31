#B2_1233_주사위

S1, S2, S3 = map(int, input().split())
freq = {}
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            s = i + j + k
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
print(max(freq, key=lambda x: (freq[x], -x)))
