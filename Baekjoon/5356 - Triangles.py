#B3_5356_Triangles

for _ in range(int(input())):
  num,ltr=map(str,input().split())

  for i in range(1,int(num)+1):
    print(ltr*i)
    if ltr=="Z":
      ltr="@"
    ltr=chr(ord(ltr)+1)

  print()
