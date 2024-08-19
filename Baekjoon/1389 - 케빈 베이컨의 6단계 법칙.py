#S1_1389_케빈 베이컨의 6단계 법칙

import sys
from collections import deque

input=sys.stdin.readline

def bacon(n,x):
  qu=deque()

  fr=[[] for _ in range(n+1)]
  res=[]

  for i in range(m):
    fr[x[i][0]].append(x[i][1])
    fr[x[i][1]].append(x[i][0])

  for i in range(1,n+1):
    visited=[False]*(n+1)
    dis=[0]*(n+1)
    qu.append(i)
    visited[i]=True

    while qu:
      k=qu.popleft()
      for nbr in fr[k]:
        if not visited[nbr]:
          qu.append(nbr)
          visited[nbr]=True
          dis[nbr]=dis[k]+1

    res.append([sum(dis),i])

  res.sort()
  return res[0][1]

n,m=map(int,input().split())
x=[]

for _ in range(m):
  a,b=map(int,input().split())
  x.append([a,b])
print(bacon(n,x))
