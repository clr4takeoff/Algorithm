#S1_1931_회의실 배정

n=int(input())
c=[]

for _ in range(n):
    s,f=map(int,input().split())
    c.append([s,f])

c.sort(key=lambda x:(x[0],x[1]))

p=c[0]
cnt=1
fin=c[0][1]

for i in range(1, n):
    if fin<=c[i][0]:
        cnt+=1
        fin = c[i][1]
    elif fin>c[i][1]:
        fin=c[i][1]

print(cnt)