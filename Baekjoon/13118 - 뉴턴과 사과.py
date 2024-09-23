#B4_13118_뉴턴과 사과

res=0
people=list(map(int,input().split()))
x,y,r=map(int,input().split())
if x in people:
  res=people.index(x)+1
print(res)
