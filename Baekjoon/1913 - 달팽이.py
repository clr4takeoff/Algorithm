#S3_1913_달팽이

n=int(input())
t=int(input())

a=[[0]*n for _ in range(n)]

x,y=0,0
num=n*n

dx=[1,0,-1,0]
dy=[0,1,0,-1]
dir=0

while num>0:
    a[x][y]=num
    if num==t:
        tx,ty=x,y
    nx=x+dx[dir]
    ny=y+dy[dir]
    if nx<0 or nx>=n or ny<0 or ny>=n or a[nx][ny]!=0:
        dir=(dir+1)%4
        nx=x+dx[dir]
        ny=y+dy[dir]
    x,y=nx,ny
    num-=1

for row in a:
    print(" ".join(map(str,row)))

print(tx+1,ty+1)
