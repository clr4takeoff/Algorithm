#S1_2178_미로 탐색

from collections import deque

def search(n,m,a):
  qu=deque()
  qu.append([0,0])

  target=[n-1,m-1]

  d=[[-1]*m for _ in range(n)]
  d[0][0]=1

  while qu:
    y,x=qu.popleft()

    for dy,dx in [[0,1], [1,0], [0,-1], [-1,0]]:
      ny,nx=y+dy,x+dx

      if 0<=ny<n and 0<=nx<m and a[ny][nx]=='1' and d[ny][nx]==-1:
        d[ny][nx]=d[y][x]+1
        qu.append([ny,nx])

  return d[n-1][m-1]

n,m=map(int,input().split())
a=[]
for _ in range(n):
  a.append(list(input()))

print(search(n,m,a))
