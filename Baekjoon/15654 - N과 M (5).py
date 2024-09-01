#S3_15654_N과 M (5)

def bt(n,m,a,seq,visited):
  if len(seq)==m:
    print(" ".join(map(str,seq)))
    return

  for i in range(n):
    if not visited[i]:
      visited[i]=True
      bt(n,m,a,seq+[a[i]],visited)
      visited[i]=False

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
visited=[False]*n
bt(n,m,a,[],visited)
