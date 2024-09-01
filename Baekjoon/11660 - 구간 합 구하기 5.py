#S1_11660_구간 합 구하기 5

import sys
input=sys.stdin.readline

def section(a,b,n,m):
  dp=[[0]*(n+1) for _ in range(n+1)]

  for i in range(1,n+1):
    for j in range(1,n+1):
      dp[i][j]=a[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]

  res=[]

  for x1,y1,x2,y2 in b:
    res.append(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])

  return res

n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
  a.append(list(map(int,input().split())))

for _ in range(m):
  b.append(list(map(int,input().split())))

res=section(a,b,n,m)
for i in range(len(res)):
  print(res[i])
