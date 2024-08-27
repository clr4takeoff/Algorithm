#S3_15652_N과 M(4)

def bt(n,m,s,seq):
  if len(seq)==m:
    print(" ".join(map(str,seq)))
    return

  for i in range(s,n+1):
    bt(n,m,i,seq+[i])

n,m=map(int,input().split())
bt(n,m,1,[])
