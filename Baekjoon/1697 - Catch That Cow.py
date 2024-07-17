#S1_1697_Catch That Cow

from collections import deque

def bfs(s, t):
  if s==t:
    return 0
  else:
    visited=[0]*100001
    qu=deque([s])
    visited[s]=0
    
    while qu:
      curr=qu.popleft()
      next=[curr-1, curr+1, curr*2]
      
      for i in next:
        if 0<=i<100001 and visited[i]==0:
          visited[i]=visited[curr]+1
          if i==t:
            return visited[i]
          qu.append(i)

n,k=map(int,input().split())
print(bfs(n,k))
