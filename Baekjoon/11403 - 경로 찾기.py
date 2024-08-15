#S1_11403_경로 찾기

def fw(n,a):
  d=[[0]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      d[i][j]=a[i][j]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if d[i][k]=="1" and d[k][j]=="1":
          d[i][j]="1"

  return d


n=int(input())
a=[]
for i in range(n):
  a.append(list(input().split()))

res=fw(n,a)

for i in res:
  print(" ".join(i))
