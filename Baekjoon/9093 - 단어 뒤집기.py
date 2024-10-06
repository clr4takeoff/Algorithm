#B1_9093_단어 뒤집기

for _ in range(int(input())):
  a=list(input().split())
  
  for i in range(len(a)):
    a[i]=list(a[i])
    a[i].reverse()
    print("".join(a[i]),end=" ")
  
  print()
