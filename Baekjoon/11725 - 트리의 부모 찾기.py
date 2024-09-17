#S2_11725_트리의 부모 찾기

from collections import deque

def dfs(n,visited,tree):
  par=[0]*(n+1)

  st=deque([1])
  visited[1]=True

  while st:
    node=st.pop()

    for nbr in tree[node]:
      if not visited[nbr]:
        visited[nbr]=True
        par[nbr]=node
        st.append(nbr)

  return par

n=int(input())
tmp=[]
tree=[[] for _ in range(n+1)]
for i in range(n-1):
  tmp.append(map(int,input().split()))

for u,v in tmp:
  tree[u].append(v)
  tree[v].append(u)

visited=[False]*(n+1)
par=dfs(n,visited,tree)

for i in range(2,n+1):
  print(par[i])
