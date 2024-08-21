#G4_14500_테트로미노

import sys
input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y,dep,sum_val):
    global max_sum
    if dep==4:
        max_sum=max(max_sum,sum_val)
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and not vis[nx][ny]:
            vis[nx][ny]=True
            dfs(nx,ny,dep+1,sum_val+brd[nx][ny])
            vis[nx][ny]=False

def chk_t(x,y):
    global max_sum
    for i in range(4):
        t_sum=brd[x][y]
        for j in range(3):
            k=(i+j)%4
            nx,ny=x+dx[k],y+dy[k]
            if not (0<=nx<n and 0<=ny<m):
                break
            t_sum+=brd[nx][ny]
        max_sum=max(max_sum,t_sum)

n,m=map(int,input().split())
brd=[list(map(int,input().split())) for _ in range(n)]
vis=[[False]*m for _ in range(n)]
max_sum=0

for i in range(n):
    for j in range(m):
        vis[i][j]=True
        dfs(i,j,1,brd[i][j])
        vis[i][j]=False
        chk_t(i,j)

print(max_sum)
