#B3_6378_Digital Roots

while True:
  n=input()
  if n=="0":
    break
  
  while len(n)>1:
    res=0
    for i in n:
      res+=int(i)
    n=str(res)

  print(n)
