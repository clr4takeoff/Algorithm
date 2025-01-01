#B2_1362_Jo’s Pet

s=1
while 1:
    o,w=map(int,input().split())
    if o==0 and w==0:break
    a=1
    while 1:
        c=input().split()
        if c[0]=='#':break
        if not a:continue
        if c[0]=='E':w-=int(c[1])
        elif c[0]=='F':w+=int(c[1])
        if w<=0:a=0
    print(f"{s} {'RIP'if not a else':-)'if o/2<w<o*2 else':-('}")
    s+=1
