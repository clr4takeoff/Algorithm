#B3_10833_사과

res=0
for _ in range(int(input())):
  people, apple = map(int,input().split())
  res+=apple%people
print(res)
