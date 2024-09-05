#S2_15666_N과 M (12)

def bt(n,m,a,s,seq,res):
  if len(seq)==m:
    res.append(seq)
    return

  prev=-1
  for i in range(s,n):
    if prev!=a[i]:
      bt(n,m,a,i,seq+[a[i]],res)
      prev=a[i]
  
  return res

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
res=bt(n,m,a,0,[],[])

for i in res:
  print(" ".join(map(str,i)))
