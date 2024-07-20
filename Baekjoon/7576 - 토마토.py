#G5_7576_토마토

from collections import deque

def ripe(m,n,box):
  t=0
  days=0
  qu=deque()

  for i in range(n):
    for j in range(m):
      if box[i][j]==1:
        qu.append([i,j])
      if box[i][j]==0:
        t+=1

  d=[[-1]*m for _ in range(n)]

  for y,x in qu:
    d[y][x]=0

  while qu:
    y,x=qu.popleft()

    for dy,dx in [[0,1], [1,0], [0,-1], [-1,0]]:
      ny,nx=y+dy,x+dx

      if 0<=ny<n and 0<=nx<m and box[ny][nx]==0 and d[ny][nx]==-1:
        d[ny][nx]=d[y][x]+1
        t-=1
        qu.append([ny,nx])
        days=max(days, d[ny][nx])

  if t>0:
    return -1
  else:
    return days


m,n=map(int,input().split())
box=[]
for _ in range(n):
  box.append(list(map(int,input().split())))
print(ripe(m,n,box))
