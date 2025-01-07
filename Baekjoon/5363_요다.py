#B3_5363_요다

n=int(input())
for _ in range(n):
 s=input().split()
 print(" ".join(s[2:]+s[:2]))
