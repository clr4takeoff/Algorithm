#B4_16727_ICPC

p1,s1=map(int,input().split())
s2,p2=map(int,input().split())
a1=p1+p2
a2=s1+s2
if a1>a2:
    print("Persepolis")
elif a1<a2:
    print("Esteghlal")
else:
    if p2>s1:
        print("Persepolis")
    elif s1>p2:
        print("Esteghlal")
    else:
        print("Penalty")
