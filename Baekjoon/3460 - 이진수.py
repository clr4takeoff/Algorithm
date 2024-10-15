#B3_3460_이진수

for _ in range(int(input())):
  a=int(input())
  a=list(str(bin(a)))
  a.reverse()
  for i in range(len(a)):
    if a[i]=="1":
      print(i, end=" ")
