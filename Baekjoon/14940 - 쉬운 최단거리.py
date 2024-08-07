#S1_14940_쉬운 최단거리

from collections import deque

def shortcut(n,m,grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                target=[i,j]
                break
    
    d=[[-1]*m for _ in range(n)]
    d[target[0]][target[1]] = 0
    
    qu=deque([target])
    
    while qu:
        y,x=qu.popleft()
        
        for dy,dx in [[0,1], [1,0], [0,-1], [-1,0]]:
            ny,nx = y+dy, x+dx
            
            if 0<=ny<n and 0<=nx<m and grid[ny][nx]==1 and d[ny][nx]==-1:
                d[ny][nx] = d[y][x]+1
                qu.append((ny, nx))
    

    for i in range(n):
        for j in range(m):
            if grid[i][j]==0:
                d[i][j]=0
    
    return d
    
n,m=map(int,input().split())
grid=[]
for i in range(n):
  grid.append(list(map(int,input().split())))

result=shortcut(n,m,grid)

for row in result:
    print(' '.join(map(str,row)))
