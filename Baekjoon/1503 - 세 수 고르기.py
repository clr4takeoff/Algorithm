#S2_1503_세 수 고르기

import sys
input=sys.stdin.readline
inf=sys.maxsize

def find_min_difference(n,s):
    res=inf
    for i in range(1,1002):
        if i in s: continue
        for j in range(1,1002):
            if j in s: continue
            for k in range(1,1002):
                if k in s: continue
                q=i*j*k
                if abs(n-q)<res:
                    res=abs(n-q)
                if n+1<q:
                    break
    return res

n,m=map(int,input().rstrip().split())
s=set(map(int,input().rstrip().split())) if m>0 else set()
print(find_min_difference(n,s))
