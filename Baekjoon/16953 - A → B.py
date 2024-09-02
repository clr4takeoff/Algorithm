#S2_16953_A → B

from collections import deque

def bfs(a,b,cnt):
  qu=deque()
  qu.append([a,cnt])

  while qu:
    a,cnt=qu.popleft()
    if a==b:
      return cnt+1
    if a<b:
      if a*2<=b:
        qu.append([a*2,cnt+1])
      qu.append([int(str(a)+"1"),cnt+1])

  return -1

def change(a,b):
  if a==b:
    return 1
  else:
    return bfs(a,b,0)

a,b=map(int,input().split())
print(change(a,b))
