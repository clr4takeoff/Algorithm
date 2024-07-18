#S2_11724_연결 요소의 개수

import sys 

def dfs(g,v,visited):
    stack=[v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for j in g[node]:
                if not visited[j]:
                    stack.append(j)

def linked(n,edges):
    g=[[] for _ in range(n+1)]
    visited=[False]*(n+1)
    cnt=0

    for u,v in edges:
        g[u].append(v)
        g[v].append(u)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(g,i,visited)
            cnt+=1

    return cnt

n,m=map(int, sys.stdin.readline().split())
edges=[list(map(int, sys.stdin.readline().split())) for _ in range(m)]
print(linked(n,edges))
