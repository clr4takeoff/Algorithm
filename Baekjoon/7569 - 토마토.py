#G5_7569_토마토

from collections import deque

def ripe(m,n,h,box):
  t=0
  days=0
  qu=deque()

  for i in range(h):
    for j in range(n):
      for k in range(m):
        if box[i][j][k]==1:
          qu.append([i,j,k])
        if box[i][j][k]==0:
          t+=1

  d=[[[-1]*m for _ in range(n)] for _ in range(h)]

  for z,y,x in qu:
    d[z][y][x]=0

  while qu:
    z,y,x=qu.popleft()

    for dz,dx,dy in [[0,0,1], [0,1,0], [0,0,-1], [0,-1,0],[1,0,0],[-1,0,0]]:
      nz,ny,nx=z+dz, y+dy, x+dx

      if 0<=nz<h and 0<=ny<n and 0<=nx<m and box[nz][ny][nx]==0 and d[nz][ny][nx]==-1:
        d[nz][ny][nx]=d[z][y][x]+1
        t-=1
        qu.append([nz,ny,nx])
        days=(max(days,d[nz][ny][nx]))

  if t>0:
    return -1
  else:
    return days

m,n,h=map(int,input().split())
box=[]

for i in range(h):
  b=[]
  for j in range(n):
    a=list(map(int,input().split()))
    b.append(a)
  box.append(b)

print(ripe(m,n,h,box))
