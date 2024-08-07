#S1_5525_IOIOI

import sys
input=sys.stdin.readline

def cnt(n,w,s):
    res=0
    idx=0
    fnd=0

    while idx<w-1:
        if s[idx]=='I':
            i=idx
            while i+2<w and s[i+1]=='O' and s[i+2]=='I':
                i+=2
                fnd+=1
                if fnd==n:
                    res+=1
                    fnd-=1
            fnd=0
            idx=i
        idx+=1

    return res

n=int(input())
w=int(input())
s=input()
print(cnt(n,w,s))
