#B3_2721_Triangular Sums

t=int(input())
for _ in range(t):
    n=int(input())
    w=0
    for k in range(1,n+1):
        t_k=(k*(k+1))//2
        t_k1=((k+1)*(k+2))//2
        w+=k*t_k1
    print(w)
