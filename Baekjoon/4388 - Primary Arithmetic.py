#B3_4388_Primary Arithmetic

while True:
  carry=0
  cnt=0
  a,b=map(str,input().split())
  if a=="0" and b=="0":
    break
  
  max_len = max(len(a),len(b))
  a=a.zfill(max_len)
  b=b.zfill(max_len)

  a=a[::-1]
  b=b[::-1]

  for i in range(max_len):
    if int(a[i])+int(b[i])+carry>=10:
      carry=1
      cnt+=1
    else:
      carry=0

  print(cnt)
