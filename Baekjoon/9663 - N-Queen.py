#G4_9663_N-Queen

def dfs(n,row,visited,d1,d2,cnt):
  if row==n:
    return cnt+1
  
  for col in range(n):
    if visited[col] or d1[row-col+n-1] or d2[row+col]:
      continue
    
    visited[col]=True
    d1[row-col+n-1]=True
    d2[row+col]=True

    cnt=dfs(n,row+1,visited,d1,d2,cnt)

    visited[col]=False
    d1[row-col+n-1]=False
    d2[row+col]=False

  return cnt

n=int(input())
visited=[False]*n
d1=[False]*(2*n-1)
d2=[False]*(2*n-1)
cnt=0
print(dfs(n,0,visited,d1,d2,cnt))
