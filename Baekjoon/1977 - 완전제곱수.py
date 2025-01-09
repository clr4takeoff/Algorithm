#B2_1977_완전제곱수

M=int(input())
N=int(input())
sq=[i*i for i in range(int(M**0.5), int(N**0.5)+1) if i*i>=M and i*i<=N]
if sq:
    print(sum(sq))
    print(min(sq))
else:
    print(-1)
