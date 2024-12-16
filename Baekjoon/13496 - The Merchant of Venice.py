#B4_13496_The Merchant of Venice

k=int(input())
for x in range(1,k+1):
    n,s,d=map(int,input().split())
    total=0
    for _ in range(n):
        di,vi=map(int,input().split())
        if di<=s*d:
            total+=vi
    print(f"Data Set {x}:")
    print(total)
    print()
