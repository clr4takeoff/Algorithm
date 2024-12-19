#B3_2783_삼각 김밥

x,y=map(int,input().split())
n=int(input())
min_cost=(x/y)*1000
for _ in range(n):
 xi,yi=map(int,input().split())
 min_cost=min(min_cost,(xi/yi)*1000)
print(f"{min_cost:.2f}")
