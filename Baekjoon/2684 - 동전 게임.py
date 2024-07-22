#B1_2684_동전 게임

coin=["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

for i in range(int(input())):
  li=[0 for i in range(8)]
  a=input()

  for i in range(38):
    s=a[0]+a[1]+a[2]

    if s in coin:
      li[coin.index(s)]+=1

    a=a[1:]

  for i in range(8):
    li[i]=str(li[i])

  print(" ".join(li))