#B3_5292_Counting Swann's Coins

n=int(input())

for i in range(1,n+1):
  if not i%3 and not i%5:
    print("DeadMan")
  elif not i%3:
    print("Dead")
  elif not i%5:
    print("Man")
  else:
    print(i,end=" ")
