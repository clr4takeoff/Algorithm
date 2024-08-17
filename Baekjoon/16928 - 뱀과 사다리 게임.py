#G5_16928_뱀과 사다리 게임

from collections import deque

def game(n,m,snake,ladder):
  qu=deque()
  qu.append([1,0])

  visited=[False]*101

  dice=[1,2,3,4,5,6]

  while qu:
    x,y=qu.popleft()
    for i in range(6):
      po,tr=x+dice[i],y+1

      for j in range(n):
        if po==ladder[j][0]:
          po=ladder[j][1]
      
      for j in range(m):
        if po==snake[j][0]:
          po=snake[j][1]

      if po==100:
          return tr

      if not visited[po]:
        visited[po]=True
        qu.append([po,tr])


n,m=map(int,input().split())
ladder=[]
snake=[]

for _ in range(n):
  x,y=map(int,input().split())
  ladder.append([x,y])

for _ in range(m):
  u,v=map(int,input().split())
  snake.append([u,v])

print(game(n,m,snake,ladder))
