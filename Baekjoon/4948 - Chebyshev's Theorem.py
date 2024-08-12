#S2_4948_Chebyshev's Theorem

import sys
import math

input=sys.stdin.readline

def era(lim):
    sieve=[True]*(lim+1)
    sieve[0]=sieve[1]=False
    for s in range(2,int(math.sqrt(lim))+1):
        if sieve[s]:
            for m in range(s*s,lim+1,s):
                sieve[m]=False
    return sieve

lim=123456*2
res=era(lim)

while True:
    n=int(input().strip())
    if n==0:
        break

    cnt=sum(res[n+1:2*n+1])
    print(cnt)